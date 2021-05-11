#!/usr/bin/env python
#


from .AbstractSvQ import AbstractSvQ as base
class GridSvQ(base):

    def __init__(self, svqhist):
        '''svqhist: a histogram instance'''
        self.svqhist = svqhist
        return

    def identify(self, visitor): return visitor.onGridSvQ( self )

    pass  # end of GridSvQ


# End of file
