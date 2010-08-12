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



class Renderer(object):


    def render(self, inventory):
        return inventory.identify(self)


    # handlers

    def onInventory(self, inventory):
        self.d = self.cd = {}
        for facility in inventory.facilities.itervalues():
            facility.identify(self)
        return self.d

    
    def onRegistry(self, registry):
        cd = self.cd
        cd['name'] = registry.name

        # bail out of empty registries
        if not registry.properties and not registry.facilities:
            return
        
        cd['components'] = {}

        for trait in registry.properties:
            value = registry.getProperty(trait)
            if trait in registry.facilities:
                cd[trait] = value
            else:
                cd[trait] = value
                
        for facility in registry.facilities:
            component = registry.getFacility(facility)
            if component:
                newd = {}
                self.cd = newd
                component.identify(self)
                cd['components'][newd['name']] = newd

        if not cd['components']:
            del cd['components']
        return


# version
__id__ = "$Id$"

# End of file 
