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
    simple_description = enginefactory.simple_description
    full_description = enginefactory.full_description

    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        
        energy = pinv.float( 'energy', default = 0) # meV
        energy.meta['tip'] = (
            'energy of the neutron. if "energy" is given, '
            'the neutron velocity will be computed so that '
            'the energy of the neutron will be the given value of energy,'
            'and the moving direction will be determined by the "velocity" vector'
            )

        energy_width = pinv.float('energy-width', default=0)
        energy_width.meta['tip'] = (
            "energy spread. if positive, there will be a normal distribution",
            "of neutron energies around the central energy.",
            "the energy_width is the standard deviation of the normal",
            "distribution.",
            )
        
        velocity = pinv.array( 'velocity', default = '0,0,3000' ) # m/s
        velocity.meta['tip'] = 'velocity of neutrons. unit: m/s. Note: if energy is nonzero, the magnitude of the velocity is set by energy'

        position = pinv.array( 'position', default = '0,0,0' )
        position.meta['tip'] = 'position of neutrons. unit: m'

        width = pinv.float('width', default=0)
        width.meta['tip'] = 'width of source. unit:m'
        
        height = pinv.float('height', default=0)
        height.meta['tip'] = 'height of source. unit:m'

        time = pinv.float( 'time', default = 0 )
        time.meta['tip'] = 'time of flight for neutrons. unit: s'

        probability = pinv.float( 'probability', default = 1. )
        probability.meta['tip'] = 'probabliity of neutrons. unit: 1'
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

        energy_width = self.inventory.energy_width
        if energy_width < 0:
            raise ValueError("energy width must be not negative")
        self.energy_width = energy_width
            
        position = self.inventory.position
        assert len(position)==3
        self.position = position
        
        self.width = self.inventory.width
        self.height = self.inventory.height

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
        self.engine = enginefactory( 
            self.name, self.neutron,
            dx = self.width, dy = self.height,
            dE = self.energy_width,
            )
        return

    pass # end of Source



# version
__id__ = "$Id$"

# End of file 
