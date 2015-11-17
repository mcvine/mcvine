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


class DispersionOnGrid:

    def __init__(
        self, axes,
        polarization_npyarr, energy_npyarr):

        self.axes = axes
        self.polarization_npyarr = polarization_npyarr
        self.energy_npyarr = energy_npyarr
        
        return

    pass # end of AbstractDispersion
    


# version
__id__ = "$Id$"

# End of file 
