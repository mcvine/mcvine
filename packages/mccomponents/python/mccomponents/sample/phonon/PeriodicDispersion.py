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


class PeriodicDispersion:

    def __init__(self, dispersion, reciprocalcell):
        self.dispersion = dispersion
        self.reciprocalcell = reciprocalcell
        self.dos = dispersion.dos
        return


    def identify(self, visitor):
        return visitor.onPeriodicDispersion(self)
    
    
    pass # end of PeriodicDispersion
    


# version
__id__ = "$Id$"

# End of file 
