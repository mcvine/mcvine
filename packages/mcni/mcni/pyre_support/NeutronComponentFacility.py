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
            return super(NeutronComponentFacility, self)._import(name)
        return component, locator

            
    def _createNeutronComponent(self, componentName):
        category, type, supplier = _decode(componentName)
        
        # component factory
        from mcni.pyre_support import findcomponentfactory
        factory = findcomponentfactory(type, category, supplier)
        
        # error handling
        if not factory:
            import journal
            journal.error("mcvine.component").log(
                "could not bind facility '%s': component factory %s not found." % (
                self.name, componentName)
                )
            return None, None
        
        # instantiate
        component = factory(self.name)
        # locator
        locator = '<mcvine.componentfactory>'
        #
        return component, locator

    pass # end of NeutronComponentFacility


def _decode(name):
    if name.find('@') == -1:
        supplier = None
        t1 = name
    else:
        t1, supplier = name.split('@')

    if t1.find('.') == -1:
        type = t1
        category = None
    else:
        type, category = t1.split('.')
    return category, type, supplier


# version
__id__ = "$Id$"

# End of file 
