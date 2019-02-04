#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
assumption:
 in each round the monitor spits out a histogram file in a output-directory-in-progress.
 all histogram files have the same filename, only the directory is different:

  <outdir>/<signature-of-progress>/<histfile>

e.g.

  out/rank0-step3/IE.h5

"""


number_mc_samples_filename = 'number_of_mc_samples'

def merge_and_normalize(histogramfilename, outdir):
    import os
    from histogram.hdf import dump
    from mpi4py import MPI
    world = MPI.COMM_WORLD
    rank = world.Get_rank()
    res = hist_mcs_sum_parallel(outdir, histogramfilename)
    if rank ==0:
        h, n = res
        h.I/=n
        h.E2/=n*n
        p = os.path.join(outdir, histogramfilename)
        dump(h, p, '/', 'c')

    if not os.environ.get('MCVINE_DEBUG_PARALLEL_PPS'): return
    # debugging. save a data file using serial mode
    if rank == 0:
        h, n = hist_mcs_sum(outdir, histogramfilename)
        h.I/=n
        h.E2/=n*n
        p = os.path.join(outdir, histogramfilename)
        p0, ext = os.path.splitext(p)
        p1 = p0+'-serial'+ext
        dump(h, p1, '/', 'c')
    return


def hist_mcs_sum(outdir, histogramfilename):
    """compute the summed histogram and summed number of mc samples"""
    import glob, os
    pattern = os.path.join(outdir, '*', histogramfilename)
    histfiles = glob.glob(pattern)
    pattern = os.path.join(outdir, '*', number_mc_samples_filename)
    mcsamplesfiles = glob.glob(pattern)
    assert len(histfiles) == len(mcsamplesfiles), "histogram files %s does not match #mcsample files %s" %(len(histfiles), len(mcsamplesfiles))
    if not histfiles:
        return None, None
    
    # load histograms
    from histogram.hdf import load
    from histogram.hdf.utils import getOnlyEntry
    loadhist = lambda f: load(f, getOnlyEntry(f))
    h1 = loadhist(histfiles[0])
    
    # XXX
    # due to a bug in h5py, we have to manually make a copy of the histogram
    # see http://code.google.com/p/h5py/issues/detail?id=121
    import histogram
    h1 = histogram.histogram(h1.name(), h1.axes(), h1.I, h1.E2)
    # XXX
    
    def _addhistfile(f):
        h = loadhist(f)
        h1.I += h.I
        h1.E2 += h.E2
        return
    map(_addhistfile, histfiles[1:])
    
    # load number_of_mc_samples
    loadmcs = lambda f: float(open(f).read())
    mcs = map(loadmcs, mcsamplesfiles)
    return h1, sum(mcs)


def hist_mcs_sum_parallel(outdir, histogramfilename):
    """compute the summed histogram and summed number of mc samples"""
    from mpi4py import MPI
    world = MPI.COMM_WORLD
    rank = world.Get_rank()
    size = world.Get_size()

    # get file lists from node 0
    if rank==0:
        import glob, os
        pattern = os.path.join(outdir, '*', histogramfilename)
        histfiles = glob.glob(pattern)
        pattern = os.path.join(outdir, '*', number_mc_samples_filename)
        mcsamplesfiles = glob.glob(pattern)
        assert len(histfiles) == len(mcsamplesfiles), "histogram files %s does not match #mcsample files %s" %(len(histfiles), len(mcsamplesfiles))
    else:
        histfiles, mcsamplesfiles = None, None
    # broadcast to all nodes
    histfiles, mcsamplesfiles = world.bcast((histfiles, mcsamplesfiles), root=0)
    # got nothing. exit
    if not histfiles:
        return None, None

    # divide the jobs
    N = len(histfiles)
    npernode = (N-1)//world.size + 1
    sl = slice(npernode*world.rank, npernode*(world.rank+1))
    histfiles1 = histfiles[sl]
    # print "%s: %s" % (world.rank, histfiles1)
    if len(histfiles1):
        # load the first one
        import histogram.hdf as hh
        h1 = hh.load(histfiles1[0])
        # remained files
        remained = histfiles1[1:]
        for f in remained:
            h = hh.load(f)
            h1.I += h.I
            h1.E2 += h.E2
            continue
        # load number_of_mc_samples
        loadmcs = lambda f: float(open(f).read())
        mcs = map(loadmcs, mcsamplesfiles[sl])
        mcs = sum(mcs)
    else:
        # no data
        # print "No data for %s" % world.rank
        h1 = None
    # merge results from all nodes
    import numpy as np
    if world.rank==0:
        h = h1
        buffer = np.empty(h1.shape(), dtype=np.float)
        for rank in range(1, world.size):
            hasdata = world.recv(source=rank, tag=120)
            if hasdata:
                world.Recv(buffer, rank, tag=121)
                h.I += buffer
                world.Recv(buffer, rank, tag=122)
                h.E2 += buffer
                mcs += world.recv(source=rank, tag=123)
            continue
    else:
        # tag:120: has data or not
        if h1 is None:
            world.send(False, 0, tag=120)
        else:
            world.send(True, 0, tag=120)
            world.Send(h1.I.astype(np.float), 0, tag=121)
            world.Send(h1.E2.astype(np.float), 0, tag=122)
            world.send(mcs, 0, tag=123)
    # wait for everybody to synchronize _here_
    world.Barrier()
    if world.rank==0:
        return h1, mcs


from outputs import mcs_sum
    

from MonitorMixin import MonitorMixin
class HistogramBasedMonitorMixin(MonitorMixin):

    def create_pps(self):
        context = self.simulation_context
        if context is None:
            raise RuntimeError, "context not defined: type - %s, name - %s" % (
                self.__class__.__name__, self.name)
        if context.mpiRank:
            return
        # create post processing script
        import os
        path = os.path.join(context.post_processing_scripts_dir, "%s.py" % self.name)
        content = """from mcni.components.HistogramBasedMonitorMixin import merge_and_normalize
merge_and_normalize(%(fn)r, %(outdir)r)
""" % dict(outdir=os.path.abspath(context.outputdir), fn=self._getHistogramFilename())
        open(path, 'wt').write(content)
        return

    def _getFinalResult(self):
        """get the final result of this monitor"""
        return self.create_pps()


    def _getHistogramFilename(self):
        raise NotImplementedError


    def _saveResult(self, res, directory):
        """save result to the given directory"""
        # this is now done in post-processing script written out
        # in method _getFinalResult
        return


# version
__id__ = "$Id$"

# End of file 
