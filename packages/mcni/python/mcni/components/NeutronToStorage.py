#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


category = 'monitors'



from mcni.neutron_storage import ndblsperneutron

from mcni.AbstractComponent import AbstractComponent

class NeutronToStorage( AbstractComponent ):


    '''Save neutrons to data files.

    This component saves neutrons to a data file
    of your choice. The data file is in the idf/Neutron format
    (svn://danse.us/inelastic/idf/Neutron.v1). You will need
    to specifiy the path of the file.
    '''


    def __init__(self, name, path, append = False):
        
        AbstractComponent.__init__(self, name)

        if not append and os.path.exists( path ):
            raise RuntimeError, "Neutron storage %r already exists. To append neutrons to this storage, please use keyword 'append=1'" % path
        
        if append: mode='a'
        else: mode = 'w'
        
        from mcni.neutron_storage import storage
        self._storage = storage( path, mode = mode)
        self.path = path
        return


    def process(self, neutrons):
        self._storage.write( neutrons )
        return neutrons


    def close(self):
        self._storage.close()
        return
    

    def create_pps(self):
        context = self.simulation_context
        if context.mpiRank != 0:
            return
        # create post processing script
        import os
        path = os.path.join(context.post_processing_scripts_dir, "%s.py" % self.name)
        content = """from mcni.components.NeutronToStorage import merge_and_normalize
merge_and_normalize(%r, %r, %r)
""" % (os.path.abspath(self.simulation_context.outputdir),
       os.path.basename(self.path),
       context.overwrite_datafiles)
        open(path, 'wt').write(content)
        return
        
    
    pass # end of NeutronToStorage


def merge_and_normalize(outdir, filename, overwrite_datafiles):
    # XXX: should rewrite using mcni.neutron_storage.merge_and_normalize
    # find all output files
    from mcni.components.outputs import n_mcsamples_files, mcs_sum
    import glob, os
    pattern = os.path.join(outdir, '*', filename)
    nsfiles = glob.glob(pattern)
    n_mcsamples = n_mcsamples_files(outdir)
    assert len(nsfiles) == n_mcsamples, \
        "neutron storage files %s does not match #mcsample files %s" %(
        len(nsfiles), n_mcsamples)
    if not nsfiles:
        return None, None

    # output
    out = os.path.join(outdir, filename)
    if overwrite_datafiles:
        if os.path.exists(out):
            os.remove(out)
    # merge
    from mcni.neutron_storage import merge
    merge(nsfiles, out)

    # number of neutron events totaly in the neutron file
    from mcni.neutron_storage.idf_usenumpy import count
    nevts = count(out)
    if nevts == 0: # no neutron saved
        return

    # load number_of_mc_samples
    mcs = mcs_sum(outdir)

    # normalization factor. this is a bit tricky!!!
    nfactor = mcs/nevts

    # normalize
    from mcni.neutron_storage import normalize
    normalize(out, nfactor)
    return

import os


# version
__id__ = "$Id$"

# End of file 
