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


from .AbstractNode import AbstractNode


class SQE_fromexpression(AbstractNode):


    tag = "SQE_fromexpression"

    def elementFactory( self, **kwds ):
        expression = str(kwds.get('expression'))
        from mccomponents.sample import sqeFromExpression
        return sqeFromExpression(expression) 

    pass # end of SQE_fromexpression


# version
__id__ = "$Id$"

# End of file 
