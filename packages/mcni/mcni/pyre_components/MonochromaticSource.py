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


from mcni.pyre_support.AbstractComponent import AbstractComponent

class MonochromaticSource( AbstractComponent ):


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        velocity = pinv.str( 'velocity', default = '0,0,3000' )
        position = pinv.str( 'position', default = '0,0,0' )
        time = pinv.float( 'time', default = 0 )
        probability = pinv.float( 'probability', default = 1. )
        pass
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        velocity = eval( self.inventory.velocity )
        assert len(velocity)==3
        self.velocity = velocity

        position = eval( self.inventory.position )
        assert len(position)==3
        self.position = position

        self.time = self.inventory.time
        self.probability = self.inventory.probability
        return


    def _init(self):
        AbstractComponent._init(self)
        from mcni import neutron
        self.neutron = neutron( r = self.position, v = self.velocity,
                                time = self.time, prob = self.probability )
        from mcni.components.MonochromaticSource import MonochromaticSource
        self.engine = MonochromaticSource( self.name, self.neutron )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
