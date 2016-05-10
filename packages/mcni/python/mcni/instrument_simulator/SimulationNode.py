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


from danse.ins.dsm.Connectable import Connectable 
class SimulationNode(Connectable):

    sockets = {
        'in': ['neutrons', 'position', 'orientation'],
        'out': ['neutrons', 'position', 'orientation'],
        }

    def __init__(
        self, position, orientation, 
        component, neutron_coordinates_transformer,
        context = None
        ):
        
        Connectable.__init__(self)
        self.position = position
        self.orientation = orientation
        self.component = component
        self.neutron_coordinates_transformer = neutron_coordinates_transformer

        # let component know the simulation context
        component.simulation_context = context
        
        process = self.component.process
        if context.multiple_scattering and hasattr(self.component, 'processM'):
            process = self.component.processM
        self.processor = self._createProcessor(
            component.name, process, tracer=context.tracer)
        
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


    def _createProcessor(self, name, process, tracer):
        from mcni import journal
        logger = journal.logger(
            'info', 'instrument', header='', footer='', format=' | %s')
        def _(neutrons):
            if tracer:
                tracer(neutrons,  context=before(self))
            # take a snapshot. it will remove the invalid neutrons from the list
            # neutrons2 = neutrons.snapshot(len(neutrons))
            # need to swap with the orignal neutron buffer
            # neutrons.swap(neutrons2)
            logger(" %s processing ..." % name)
            process(neutrons)
            if tracer:
                tracer(neutrons,  context=processed(self))
            return neutrons
        return _


    pass # end of SimulationNode
        


class context(object):

    def __init__(self, obj):
        self.obj = obj


class before(context): 
    def identify(self, visitor): return visitor.onBefore(self)

class processed(context): 
    def identify(self, visitor): return visitor.onProcessed(self)


# version
__id__ = "$Id$"

# End of file 
