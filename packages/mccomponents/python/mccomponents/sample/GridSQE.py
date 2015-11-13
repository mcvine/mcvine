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


from AbstractSQE import AbstractSQE as base
class GridSQE(base):

    def __init__(self, sqehist):
        '''sqehist: a histogram instance'''
        self.sqehist = sqehist
        return
    
    def identify(self, visitor): return visitor.onGridSQE( self )

    pass  # end of AbstractSQE


# version
__id__ = "$Id$"

# End of file 
