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
    
    onSQEkernel = onKernelContainer = AbstractNode.onElement

    def elementFactory(self, *args, **kwds):
        from mccomponents.sample import kernelcontainer
        return kernelcontainer( )

    pass # end of KernelContainer
    


# version
__id__ = "$Id: KernelContainer.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
