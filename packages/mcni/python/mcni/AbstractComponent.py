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





class AbstractComponent:


    '''base class of Monte Carlo neutron components'''



    def __init__(self, name):
        self.name = name
        # simulation context. this will be assigned by the simulator
        self.simulation_context = None
        return
    
    
    def process(self, neutrons):
        raise NotImplementedError


    def create_pps(self):
        "create post-processing script in given dir"
        # overload this to provide the functionality for a specific component type
        return


    def _get_overwrite_datafiles(self):
        import warnings
        msg = "In %s: Deprecated. should use self.simulation_context.overwrite_datafiles" %(
            self.__class__.__name__)
        warnings.warn(msg)
        return self.simulation_context.overwrite_datafiles

    def _set_overwrite_datafiles(self, v):
        raise RuntimeError
    overwrite_datafiles = property(_get_overwrite_datafiles, _set_overwrite_datafiles)


    def _getOutputDir(self):
        "get the output directory of the simulation"
        simulation_context = self.simulation_context
        if simulation_context is None:
            raise RuntimeError('simulation context was not defined. Type: %s, Name: %s' % (
                self.__class__.__name__, self.name))
        return self.simulation_context.outputdir


    def _getOutputDirInProgress(self):
        '''get output directory when simulation is in progress.
        It depends on the computing node, and also the iteration #.
        this is different from _getOutputDir which is the output dir
        for final products
        '''
        context = self.simulation_context
        return context.getOutputDirInProgress()
    
        
    def _runInDir(self, func, dir):
        """run the given function in the given directory"""
        return run_in_dir(func, dir)


    pass # AbstractComponent


import os

class ChangeDirectory:


    def __init__(self, dir):
        self.dir = dir
        return

    def __enter__(self):
        import os
        self.savedir = os.path.abspath(os.curdir)
        os.chdir(self.dir)
        return self


    def __exit__(self, type, value, traceback):
        os.chdir(self.savedir)
        return


def run_in_dir(func, dir):
    with ChangeDirectory(dir):
        ret = func()
    return ret



# version
__id__ = "$Id$"

# End of file 
