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


class KernelComputingEngineFactory(object):

    def __init__(self, binding):
        self.binding = binding
        return


    def composite(self, kernels):
        return self.binding.composite( kernels )


    def kernelcontainer(self):
        return self.binding.kernelcontainer( )


    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            return getattr(self.binding, name)    

    pass # end of KernelComputingEngineFactory


# version
__id__ = "$Id$"

# End of file 
