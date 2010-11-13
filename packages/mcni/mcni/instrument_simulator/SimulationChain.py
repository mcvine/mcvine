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


from dsm.Composite import Composite 
class SimulationChain(Composite):

    sockets = {
        'in': ['neutrons', 'position', 'orientation'],
        'out': ['neutrons', 'position', 'orientation'],
        }

    def __init__(
        self, 
        components, geometer, 
        neutron_coords_transformer, 
        multiple_scattering=False,
        tracer = None,
        ):

        components, geometer = self._enclosure( components, geometer )
        
        nodes, connections = self._create(
            components, geometer, neutron_coords_transformer, 
            multiple_scattering=multiple_scattering,
            tracer = tracer
            )
        
        Composite.__init__(self, nodes, connections)

        self.setInput('position', (0,0,0))
        self.setInput('orientation', (0,0,0))
        return


    def _enclosure(self, components, geometer):
        from mcni.DummyComponent import DummyComponent
        begin = DummyComponent('dummyBegin')
        end = DummyComponent('dummyEnd')
        components = [begin] + components + [end]
        geometer.register( begin, (0,0,0), (0,0,0) )
        geometer.register( end, (0,0,0), (0,0,0) )
        return components, geometer


    def _create(
        self, 
        components, geometer, 
        neutron_coords_transformer, 
        multiple_scattering=False,
        tracer = None,
        ):
        from SimulationNode import SimulationNode

        nodes = {}
        connections = []
        previous = 'self'

        for component in components:

            position = geometer.position( component )
            orientation = geometer.orientation( component )
            nodes[component.name] = SimulationNode(
                position, orientation, component, neutron_coords_transformer,
                multiple_scattering = multiple_scattering,
                tracer = tracer)

            now = component.name

            if isabstract(component):
                raise "component %s at %s, rotated %s is abstract" % (
                    now, position, orientation)

            newconnetions = self._connections( previous, now )
            connections += newconnetions

            previous = now
            continue

        connections += self._connections( components[-1].name, 'self')

        return nodes, connections


    def _connections(self, comp1, comp2 ):
        connetions = [
            '%s:neutrons->neutrons:%s' % (comp1, comp2),
            '%s:position->position:%s' % (comp1, comp2),
            '%s:orientation->orientation:%s' % (comp1, comp2),
            ]
        return connetions


    pass # end of SimulationChain


from mcni.AbstractComponent import AbstractComponent
def isabstract(component):
    return component.__class__ is AbstractComponent
        

# version
__id__ = "$Id$"

# End of file 
