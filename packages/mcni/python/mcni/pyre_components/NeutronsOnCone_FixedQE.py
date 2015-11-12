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


from mcni.components.NeutronsOnCone_FixedQE import \
     NeutronsOnCone_FixedQE as enginefactory, category
     


from mcni.pyre_support.AbstractComponent import AbstractComponent


class NeutronsOnCone_FixedQE(AbstractComponent):

    class Inventory(AbstractComponent.Inventory):

        import pyre.inventory

        Q = pyre.inventory.float('Q', default = 5 )
        Q.meta['tip'] = 'momentum transfer. unit: angstrom^-1'

        E = pyre.inventory.float('E', default = 20 )
        E.meta['tip'] = 'energy transfer. unit: meV'
        
        Ei = pyre.inventory.float('Ei', default = 60 )
        Ei.meta['tip'] = 'incident energy. unit: meV'
        
        L1 = pyre.inventory.float('L1', default = 10 )
        L1.meta['tip'] = 'Distance from moderator to sample. unit: meter'
        
        pass


    def __init__(self, name="fixedqe"):
        AbstractComponent.__init__(self, name)
        return


    def process(self, neutrons):
        return self.engine.process( neutrons )
    

    def _configure(self):
        AbstractComponent._configure(self)
        Ei = self.inventory.Ei
        E = self.inventory.E
        Q = self.inventory.Q
        L1 = self.inventory.L1

        self.engine = enginefactory( self.name, Q, E, Ei, L1 )
        return

    
    pass # end of  NeutronsOnCone_FixedQE
