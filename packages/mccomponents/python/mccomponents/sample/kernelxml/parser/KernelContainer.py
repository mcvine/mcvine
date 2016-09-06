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


from .KernelNode import KernelNode as base, debug

# KernelContainer is just an alias of CompositKernel
# why not just reuse the CompositKernel parser node?
# the implementation here is different from CompositKernel,
# and it reuses the implementation methods in AbstractNode
class KernelContainer(base):


    tag = "KernelContainer"
    
    
    def __getattr__(self, key):
        if key.startswith('on') and key.endswith('Kernel'):
            return self.onElement
        raise
    
    
    onIsotropicKernel \
        = onConstantQEKernel = onConstantvQEKernel \
        = onConstantEnergyTransferKernel \
        = onE_Q_Kernel = onBroadened_E_Q_Kernel = onE_vQ_Kernel \
        = onSQEkernel \
        = onDGSSXResKernel \
        = onKernelContainer = base.onElement

    def createKernel(self, *args, **kwds):
        average = kwds.get('average')
        if average:
            average = average.lower() in ['1', 'on', 'yes', 'true']
            kwds['average'] = average
        from mccomponents.sample import kernelcontainer
        return kernelcontainer(*args, **kwds)

    pass # end of KernelContainer
    


# version
__id__ = "$Id$"

# End of file 
