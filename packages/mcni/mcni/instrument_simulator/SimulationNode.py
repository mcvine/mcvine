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


from dsm.Connectable import Connectable 
class SimulationNode(Connectable):

    sockets = {
        'in': ['neutrons', 'position', 'orientation'],
        'out': ['neutrons', 'position', 'orientation'],
        }

    def __init__(self, position, orientation, component, neutron_coordinates_transformer):
        Connectable.__init__(self)
        self.position = position
        self.orientation = orientation
        self.component = component
        self.neutron_coordinates_transformer = neutron_coordinates_transformer
        return


    def _update(self):
        neutrons = self._inputs['neutrons']
        position = self._inputs['position']
        orientation = self._inputs['orientation']
        
        self.neutron_coordinates_transformer(
            neutrons,
            position, orientation,
            self.position, self.orientation)
        
        self.component.process(neutrons)
        
        self._outputs['neutrons'] = neutrons
        self._outputs['position'] = self.position
        self._outputs['orientation'] = self.orientation
        return

    pass # end of SimulationNode
        


# version
__id__ = "$Id$"

# End of file 
