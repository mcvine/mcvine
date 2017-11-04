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
    h, n = hist_mcs_sum(outdir, histogramfilename)
    h.I/=n
    h.E2/=n*n
    import os
    p = os.path.join(outdir, histogramfilename)
    from histogram.hdf import dump
    dump(h, p, '/', 'c')
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


from outputs import mcs_sum
    

from MonitorMixin import MonitorMixin
class HistogramBasedMonitorMixin(MonitorMixin):

    def _getFinalResult(self):
        """get the final result of this monitor"""
        context = self.simulation_context
        if context is None:
            raise RuntimeError, "context not defined: type - %s, name - %s" % (
                self.__class__.__name__, self.name)
        if context.mpiRank != 0:
            return
        # create post processing script
        import os
        path = os.path.join(context.post_processing_scripts_dir, "%s.py" % self.name)
        content = """from mcni.components.HistogramBasedMonitorMixin import merge_and_normalize
merge_and_normalize(%(fn)r), %(outdir)r)
""" % dict(outdir=os.path.abspath(context.outputdir), fn=self._getHistogramFilename())
        open(path, 'wt').write(content)
        return


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
