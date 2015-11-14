#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# this is not a good implementation
# this assumes that all _fini steps will be performed
# in the _outputdir directory.
# for now this seems to be no problem, but this
# might be vulnerable.

from mcni.pyre_support.AbstractComponent import AbstractComponent


class ComponentInterface(AbstractComponent):

    
    def process(self, neutrons):
        return self.engine.process(neutrons)


    def _hasEngine(self):
        return self.__dict__.get('engine')

    
# version
__id__ = "$Id$"

# End of file 
