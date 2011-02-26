#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



# inherit from this class in addition to the Actor class will make the actor
# capable of accepting any inputs in the inventory without the need to
# explicitly declare the input
class AcceptArbitraryInputMixin:


    def updateConfiguration(self, registry):
        listing = self._listing(registry)
        if listing:
            for k, v in listing:
                setattr(self.inventory, k, v)        
        return []

    
    def _listing(self, registry):
        if not registry: return []
        listing = [
            (name, descriptor.value) for name, descriptor in registry.properties.iteritems()
            ]

        listing += [
            ("%s.%s" % (nodename, name), value)
            for nodename, node in registry.facilities.iteritems()
            for name, value in self._listing(node)
            ]

        return listing



from mcni.pyre_support.AbstractComponent import AbstractComponent
class VitessBase(AcceptArbitraryInputMixin, AbstractComponent):
    
    supplier = 'vitess'
    category = 'optics'
    type = 'Vitess'

    class Inventory(AbstractComponent.Inventory):
        
        import pyre.inventory
        


def vitess(modulename=None):
    '''
    vitess("chopper_fermi_Linux")
    '''

    class Vitess(VitessBase):

        if modulename:
            simple_description = "vitess component %s" % modulename
        else:
            simple_description = "vitess component"
        simple_description += "  ** this component is experimental **"

        if modulename:
            full_description = ""
        else:
            full_description = (
                "You have not specified 'modulename'."
                )

        class Inventory( VitessBase.Inventory ):

            import pyre.inventory


        def process(self, neutrons):
            ret = self.engine.process( neutrons )
            return ret


        def _init(self):
            super(Vitess, self)._init()
            if not self._showHelpOnly:
                self._createEngineArgs()
                self._createEngine()
            return

        
        def _createEngineArgs(self):
            name = self.inventory.name
            args = [name, modulename]
            kwds = {}
            for k, v in self.inventory.__dict__:
                if k.startswith('_'): continue
                kwds[k] = v
                continue
            self._engine_args = args, kwds
            return


        def _createEngine(self):
            from ..components.Vitess import Vitess
            args, kwds = self._engine_args
            self.engine = Vitess(*args, **kwds)
            return

        pass
    
    return Vitess


# version
__id__ = "$Id$"

# End of file 
