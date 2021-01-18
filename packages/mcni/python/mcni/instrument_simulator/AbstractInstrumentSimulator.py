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

    def run(self, neutrons, instrument, geometer, 
            context = None):

        # save the number of neutrons
        nneutrons = len(neutrons)
        # save context
        self.context = context
        
        # provide seeds to all random number generators
        from mcni.seeder import feed
        feed()
        
        components = instrument.components

        runnable = self.makeRunnable( 
            components, geometer, 
            context = context,
            )

        runnable.setInput('neutrons', neutrons)
        runnable.getOutput( 'neutrons' )

        self.recordNumberOfMCSamples(nneutrons)
        return
        

    def recordNumberOfMCSamples(self, n):
        # write out the number of mc samples processed
        context = self.context
        outdir = context.getOutputDirInProgress()
        if outdir is None:
            return
        import os
        p = os.path.join(outdir, 'number_of_mc_samples')
        with open(p, 'w') as stream:
            stream.write(str(n))
        return


    def makeRunnable(
        self, 
        components, geometer, 
        context = None,
        ):

        neutron_coordinates_transformer = self.neutron_coordinates_transformer
        
        from .SimulationChain import SimulationChain
        chain = SimulationChain( 
            components, geometer, neutron_coordinates_transformer, 
            context = context,
            )
        
        return chain
    

    pass # AbstractInstrumentSimulator


# version
__id__ = "$Id$"

# End of file 
