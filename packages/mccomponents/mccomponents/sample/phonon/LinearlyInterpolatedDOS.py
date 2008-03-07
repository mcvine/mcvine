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


from AbstractDOS import AbstractDOS as base
class LinearlyInterpolatedDOS(base):

    def __init__(self, doshist):
        '''doshist: a histogram instance'''
        self.doshist = doshist
        return
    
    def identify(self, visitor): return visitor.onLinearlyInterpolatedDOS( self )

    pass  # end of AbstractDOS


# version
__id__ = "$Id$"

# End of file 
