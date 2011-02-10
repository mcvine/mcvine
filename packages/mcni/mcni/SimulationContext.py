#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2011  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


# context for mc simulation of a neutron instrument


class SimulationContext:

    def __init__(self, multiple_scattering=False, tracer=None, iteration_no=None, outputdir=None,
                 mpiRank=None, mpiSize=None):
        self.multiple_scattering = multiple_scattering
        self.tracer = tracer
        self.iteration_no = iteration_no
        self.outputdir = outputdir
        self.mpiRank = mpiRank
        self.mpiSize = mpiSize
        return


    def getOutputDirInProgress(self):
        '''get output directory when simulation is in progress.
        It depends on the computing node, and also the iteration #.
        this is different from property "outputdir" which is the output dir
        for final products
        '''
        import os
        if self.mpiSize:
            dir = 'rank%s-step%s' % (self.mpiRank, self.iteration_no)
        else:
            dir = 'step%s' % (self.iteration_no,)
            
        dir = os.path.join(self.outputdir, dir)
        
        if not os.path.exists(dir):
            os.makedirs(dir)

        return dir
    
        

# version
__id__ = "$Id$"

#  End of file 
