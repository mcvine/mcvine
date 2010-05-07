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


from AbstractNode import AbstractNode, debug


class IsotropicKernel(AbstractNode):


    tag = "IsotropicKernel"

    def elementFactory( self, **kwds ):
        from mccomponents.sample import isotropickernel
        return isotropickernel()


    pass # end of IsotropicKernel


# version
__id__ = "$Id$"

# End of file 
