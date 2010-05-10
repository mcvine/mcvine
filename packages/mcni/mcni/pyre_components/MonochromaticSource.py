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


from mcni.components.MonochromaticSource import MonochromaticSource as enginefactory, category

from mcni.pyre_support.AbstractComponent import AbstractComponent


class MonochromaticSource( AbstractComponent ):

    __doc__ = enginefactory.__doc__

    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        
        energy = pinv.float( 'energy', default = 0) # meV
        energy.meta['tip'] = (
            'energy of the neutron. if "energy" is given, '
            'the neutron velocity will be computed so that '
            'the energy of the neutron will be the given value of energy,'
            'and the moving direction will be determined by the "velocity" vector'
            )
        velocity = pinv.array( 'velocity', default = '0,0,3000' ) # m/s
        position = pinv.array( 'position', default = '0,0,0' )
        time = pinv.float( 'time', default = 0 )
        probability = pinv.float( 'probability', default = 1. )
        pass
    

    def process(self, neutrons):
        return self.engine.process( neutrons )


    def _configure(self):
        AbstractComponent._configure(self)
        velocity =  self.inventory.velocity
        assert len(velocity)==3
        self.velocity = velocity

        energy = self.inventory.energy
        if energy:
            from mcni.utils.conversion import e2v
            v = e2v(energy)
            import numpy.linalg as nl, numpy as np
            norm = nl.norm(velocity)
            velocity = np.array(velocity)
            velocity *= v/norm
            self.velocity = velocity
            
        position = self.inventory.position
        assert len(position)==3
        self.position = position

        self.time = self.inventory.time
        self.probability = self.inventory.probability
        return


    def _init(self):
        AbstractComponent._init(self)
        from mcni import neutron
        self.neutron = neutron(
            r = self.position, v = self.velocity,
            time = self.time, prob = self.probability,
            )
        self.engine = enginefactory( self.name, self.neutron )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
