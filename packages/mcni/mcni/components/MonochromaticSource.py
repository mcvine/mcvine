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


from mcni.AbstractComponent import AbstractComponent

class MonochromaticSource( AbstractComponent ):


    def __init__(self, name, neutron):
        AbstractComponent.__init__(self, name)
        self.neutron = neutron
        return


    def process(self, neutrons):
        neutron = self.neutron
        for i in range(len(neutrons)): neutrons[i] = neutron
        return neutrons


    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
