#!/usr/bin/env python
#
#


from .AbstractNode import AbstractNode


class SQ_fromexpression(AbstractNode):


    tag = "SQ_fromexpression"

    def elementFactory( self, **kwds ):
        expression = kwds.get('expression')
        from mccomponents.sample import sqFromExpression
        return sqFromExpression(expression) 

    pass # end of SQ_fromexpression


# End of file 
