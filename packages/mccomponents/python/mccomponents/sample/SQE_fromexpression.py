#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .AbstractSQE import AbstractSQE as base
class SQE_fromexpression(base):

    def __init__(self, expression):
        '''expression: an analystic expression of S(Q,E) function'''
        self.expression = expression
        return
    
    def identify(self, visitor): return visitor.onSQE_fromexpression( self )

    pass  # end of SQE_fromexpression


# version
__id__ = "$Id$"

# End of file 
