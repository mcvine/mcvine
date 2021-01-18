#!/usr/bin/env python
#
#


from .AbstractSQ import AbstractSQ as base
class SQ_fromexpression(base):

    def __init__(self, expression):
        '''expression: an analystic expression of S(Q) function'''
        self.expression = expression
        return
    
    def identify(self, visitor): return visitor.onSQ_fromexpression( self )

    pass  # end of SQ_fromexpression


# End of file 
