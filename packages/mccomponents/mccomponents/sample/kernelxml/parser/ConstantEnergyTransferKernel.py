#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


class ConstantEnergyTransferKernel(AbstractNode):


    tag = "ConstantEnergyTransferKernel"

    def elementFactory( self, **kwds ):
        from mccomponents.sample import constantEnergyTransferKernel
        E = self._parse( kwds['energy-transfer'] )
        return constantEnergyTransferKernel(E)
    
    
    pass # end of ConstantEnergyTransferKernel


# version
__id__ = "$Id$"

# End of file 
