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


# Mixin for a composite neutron component, which contains several components


class CompositeNeutronComponentMixin(object):


    def _find_all_neutron_subcomponents(self):
        # find all neutron sub-components
        neutron_components = {}
        for name in self.inventory.facilityNames():
            comp = self.inventory.getTraitValue( name )
            if isinstance(comp, McniComponent):
                neutron_components[ name ] = comp
                pass
            continue
        self.neutron_components = neutron_components
        
        return


    pass # end of CompositeNeutronComponentMixin


from mcni.AbstractComponent import AbstractComponent as McniComponent


# version
__id__ = "$Id$"

# End of file 
