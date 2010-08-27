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


class ConstantQEKernel(AbstractNode):


    tag = "ConstantQEKernel"

    def elementFactory( self, **kwds ):
        from mccomponents.sample import constantQEKernel
        E = self._parse( kwds['energy-transfer'] )
        Q = self._parse( kwds['momentum-transfer'] )
        return constantQEKernel(Q, E)
    
    
    pass # end of ConstantQEKernel


# version
__id__ = "$Id$"

# End of file 
