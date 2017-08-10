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
        from .utils import nice_dos
        E, g = nice_dos(doshist.energy, doshist.I, force_fitparabolic=True)
        import histogram
        self.doshist =  histogram.histogram(
            'dos', 
            [('energy', E, 'meV')],
            g)
        return
    
    def identify(self, visitor): return visitor.onLinearlyInterpolatedDOS( self )

    pass  # end of AbstractDOS


# version
__id__ = "$Id$"

# End of file 
