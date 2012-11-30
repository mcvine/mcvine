#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode


class KernelContainer(AbstractNode):


    tag = "KernelContainer"
    
    
    def __getattr__(self, key):
        if key.startswith('on') and key.endswith('Kernel'):
            return self.onElement
        raise
    
    
    onIsotropicKernel \
        = onConstantQEKernel = onConstantEnergyTransferKernel \
        = onE_Q_Kernel = onBroadened_E_Q_Kernel \
        = onSQEkernel \
        = onKernelContainer = AbstractNode.onElement

    def elementFactory(self, *args, **kwds):
        from mccomponents.sample import kernelcontainer
        return kernelcontainer( )

    pass # end of KernelContainer
    


# version
__id__ = "$Id$"

# End of file 
