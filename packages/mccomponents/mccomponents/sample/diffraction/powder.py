#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class Peak:

    "a powder diffraction peak"

    q = 0
    F_squared = 0
    multiplicity = 0
    intrinsic_line_width = 0
    DebyeWaller_factor = 0
    
    def __init__(self, **kwds):
        for k, v in kwds.iteritems():
            setattr(self, k, v)
            continue
        return


    def __repr__(self):
        return "Peak(q=%s, F_squared=%s, multiplicity=%s, intrinsic_line_width=%s, DebyeWaller_factor=%s" % (
            self.q, self.F_squared, self.multiplicity, self.intrinsic_line_width, self.DebyeWaller_factor)


# version
__id__ = "$Id$"

# End of file 
