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


class AbstractInstrumentSimulator:


    '''run simulation of an instrument'''

    
    # overload this so that it is not abstract
    # take a look at mcni.AbstractNeutronCoordinatesTransformer for interface
    neutron_coordinates_transformer = None 

    
    def run(self, neutrons, instrument, geometer):

        # provide seeds to all random number generators
        from mcni.seeder import feed
        feed()
        
        components = instrument.components

        runnable = self.makeRunnable( components, geometer )

        runnable.setInput('neutrons', neutrons)
        runnable.getOutput( 'neutrons' )
        
        return


    def makeRunnable(self, components, geometer):

        neutron_coordinates_transformer = self.neutron_coordinates_transformer
        
        from SimulationChain import SimulationChain
        chain = SimulationChain( components, geometer, neutron_coordinates_transformer )
        
        return chain
    

    pass # AbstractInstrumentSimulator


# version
__id__ = "$Id$"

# End of file 
