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

    
    class Inventory(AbstractComponent.Inventory):

        import pyre.inventory
        restore_neutron = pyre.inventory.bool('restore_neutron')


    def process(self, neutrons):
        self.engine.simulation_context = self.simulation_context
        # self.engine is created by self._createEngine()
        # earlier in self._init.
        # See mcstas2.utils.pyre_support.ElementaryComponentGenerator
        # self.engine should be an instance of mcstas2.AbstractComponent.AbstractComponent
        # and are created by factories methods registered in
        # mcstas2.components.Registry
        self.engine.restore_neutron = self.inventory.restore_neutron
        return self.engine.process(neutrons)


    def _hasEngine(self):
        return self.__dict__.get('engine')


# End of file 
