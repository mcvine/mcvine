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

    def __init__(
        self, position, orientation, 
        component, neutron_coordinates_transformer,
        multiple_scattering=False,
        tracer = None
        ):
        
        Connectable.__init__(self)
        self.position = position
        self.orientation = orientation
        self.component = component
        self.neutron_coordinates_transformer = neutron_coordinates_transformer
        self.multiple_scattering = multiple_scattering

        process = self.component.process
        if self.multiple_scattering and hasattr(self.component, 'processM'):
            process = self.component.processM
        self.processor = _createProcessor(process, tracer=tracer)
        
        return


    def __str__(self):
        return '%s(simulation node)' % self.component.name


    def _update(self):
        neutrons = self._inputs['neutrons']
        position = self._inputs['position']
        orientation = self._inputs['orientation']
        
        self.neutron_coordinates_transformer(
            neutrons,
            position, orientation,
            self.position, self.orientation)


        try:
            self.processor(neutrons)
        except NotImplementedError:
            raise NotImplementedError, "component %s at %s rotated %s has not implemented method 'process'" % (
                self.component.name, position, orientation)
        
        self._outputs['neutrons'] = neutrons
        self._outputs['position'] = self.position
        self._outputs['orientation'] = self.orientation
        return

    pass # end of SimulationNode
        


def _createProcessor(process, tracer):
    def _(neutrons):
        process(neutrons)
        if tracer:
            tracer(neutrons)
        return neutrons
    return _


# version
__id__ = "$Id$"

# End of file 
