#!/usr/bin/env python
#


from AbstractSQ import AbstractSQ as base
class GridSQ(base):

    def __init__(self, sqhist):
        '''sqhist: a histogram instance'''
        self.sqhist = sqhist
        return
    
    def identify(self, visitor): return visitor.onGridSQ( self )

    pass  # end of GridSQ


# End of file 
