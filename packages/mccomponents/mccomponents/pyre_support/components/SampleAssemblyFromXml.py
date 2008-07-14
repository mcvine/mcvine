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
        xml = pinv.str( 'xml', default = 'sampleassembly.xml' )
        pass
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        self.xml = self.inventory.xml
        return


    def _init(self):
        AbstractComponent._init(self)
        if self._showHelpOnly: return
        self.engine = enginefactory(
            self.name, self.xml) 
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
