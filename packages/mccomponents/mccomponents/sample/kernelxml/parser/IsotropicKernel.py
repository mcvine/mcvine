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


class IsotropicKernel(base):


    tag = "IsotropicKernel"

    def createKernel( self, **kwds ):
        from mccomponents.sample import isotropickernel
        return isotropickernel()


    pass # end of IsotropicKernel


# version
__id__ = "$Id$"

# End of file 
