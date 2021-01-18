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


category = 'monitors'


from mcni.AbstractComponent import AbstractComponent

class NeutronPrinter( AbstractComponent ):

    def process(self, neutrons):
        for n in neutrons: print(n)
        return

    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
