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



from mccomponents.sample import samplecomponent as enginefactory
from mcni.pyre_support.AbstractComponent import AbstractComponent


class SampleAssemblyFromXml( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        xml = pinv.str( 'xml', default = '' )
        pass
    

    def process(self, neutrons):
        engine = self.engine
        if not engine:
            raise RuntimeError, "engine not initialized"
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        self.xml = self.inventory.xml
        return


    def _init(self):
        AbstractComponent._init(self)
        if self._showHelpOnly: return
        if self.xml:
            self.engine = enginefactory(
                self.name, self.xml)
        else:
            self.engine = None
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
