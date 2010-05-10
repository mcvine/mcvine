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


from pyre.inventory.Facility import Facility


class NeutronComponentFacility( Facility ):


    def _import(self, name):
        component, locator = self._createNeutronComponent(name)
        if component is None:
            component, locator = super(NeutronComponentFacility, self)._import(name)
        return component, locator

            
    def _createNeutronComponent(self, componentName):
        category, type, supplier = _decode(componentName)
        from mcni.pyre_support import componentfactory
        factory = componentfactory(category, type, supplier)
        component = factory(self.name)
        return component, 'mcvine.componentfactory'

    pass # end of NeutronComponentFacility


def _decode(name):
    t1, supplier = name.split('@')
    type, category = t1.split('.')
    return category, type, supplier


# version
__id__ = "$Id$"

# End of file 
