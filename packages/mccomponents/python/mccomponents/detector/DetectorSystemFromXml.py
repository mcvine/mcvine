"""
A proxy class for DetectorSytem cpp instance
"""

import sys
from mcni.AbstractComponent import AbstractComponent


class DetectorSystemFromXml(AbstractComponent):


    def __init__(self, cpp_instance, eventsdat):
        self._cpp_instance = cpp_instance
        self.eventsdat = eventsdat
        return


    def process(self, neutrons):
        outdir = self.simulation_context.getOutputDirInProgress() or ''
        import os
        if not os.path.isabs(outdir):
            outdir = os.path.abspath(outdir)
        path = os.path.join(outdir, self.eventsdat)
        if sys.version_info < (3,0) and isinstance(path, unicode):
            path = path.encode()
        self.mca.setOutputFile(path)
        return self._cpp_instance.process(neutrons)


    def create_pps(self):
        context = self.simulation_context
        if context.mpiRank:
            return
        # create post processing script
        import os
        path = os.path.join(context.post_processing_scripts_dir, "%s.py" % self.name)
        content = """from mccomponents.detector.DetectorSystemFromXml import merge_and_normalize
merge_and_normalize(%r, %r, %r)
""" % (os.path.abspath(self.simulation_context.outputdir),
       os.path.basename(self.eventsdat),
       self.simulation_context.overwrite_datafiles)
        open(path, 'wt').write(content)
        return


    def __getattr__(self, name):
        return getattr(self._cpp_instance, name)


def merge_and_normalize(
    outputdir='out',
    eventsdat='events.dat',
    overwrite_datafiles=True):
    # just do it in serial mode for now
    from mpi4py import MPI
    world = MPI.COMM_WORLD
    rank = world.Get_rank()
    if rank ==0:
        merge_and_normalize_serial(outputdir, eventsdat, overwrite_datafiles)
    return
    
    
class Storage_MCsample_Mismatch(Exception): pass
def merge_and_normalize_serial(
    outputdir='out',
    eventsdat='events.dat',
    overwrite_datafiles=True):
    
    # find all output files
    from mcni.components.outputs import n_mcsamples_files, mcs_sum
    import glob, os
    filename = eventsdat
    pattern = os.path.join(outputdir, '*', filename)
    eventdatfiles = glob.glob(pattern)
    n_mcsamples = n_mcsamples_files(outputdir)
    if len(eventdatfiles) != n_mcsamples:
        msg = "neutron storage files %s does not match #mcsample files %s" %(
            len(eventdatfiles), n_mcsamples)
        raise Storage_MCsample_Mismatch(msg)
    if not eventdatfiles:
        return

    # output
    out = os.path.join(outputdir, eventsdat)
    if overwrite_datafiles:
        if os.path.exists(out):
            os.remove(out)
    # merge
    from mccomponents.detector import mergeEventFiles
    mergeEventFiles(eventdatfiles, out)
    
    # load number_of_mc_samples
    mcs = mcs_sum(outputdir)
    # normalize
    from mccomponents.detector import normalizeEventFile
    normalizeEventFile(out, mcs)
    return


    
