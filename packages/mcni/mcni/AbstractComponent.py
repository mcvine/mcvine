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


    def _getOutputDir(self):
        "get the output directory of the simulation"
        return self.simulation_context.outputdir


    def _getOutputDirInProgress(self):
        '''get output directory when simulation is in progress.
        this is different from _getOutputDir which is the output dir
        for final products
        '''
        context = self.simulation_context
        if context.mpiSize:
            dir = 'rank%s-step%s' % (context.mpiRank, context.iteration_no)
        else:
            dir = 'step%s' % (context.iteration_no,)

        dir = os.path.join(context.outputdir, dir)
        
        if not os.path.exists(dir):
            os.makedirs(dir)

        return dir
    
        
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
