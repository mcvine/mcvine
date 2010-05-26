#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

__doc__ = """ARCS instrument"""
__author__ = 'Jiao Lin'



import mcvine

from mcni.pyre_support.Instrument import Instrument as base
class Moderator2Sample(base):

    class Inventory(base.Inventory):
        
        #neutron components
        #moderator
        from mcni.pyre_support import facility
        moderator = facility('moderator', default = 'sns_moderator_beamline18')

        #guides 
        core_vessel_insert = facility(
            'core_vessel_insert', default = 'core_vessel_insert')
        
        shutter_guide  = facility(
            'shutter_guide', default = 'shutter_guide')
        
        guide1 = facility('guide1', default = 'guide1')

        # T0 chopper
        # should change this to a real t0 chopper
        t0_chopper = facility('t0_chopper', default = 't0_chopper')

        # guide
        guide2 = facility('guide2', default = 'guide2')

        #Fermi chopper
        fermi_chopper = facility(
            'fermi_chopper', default = 'fermi_chopper')

        #guides
        guide3 = facility('guide3', default = 'guide3')
        guide4 = facility('guide4', default = 'guide4')
        guide5 = facility('guide5', default = 'guide5')

        #monitors
        energy_monitor1 = facility(
            'energy_monitor1', default = 'energy_monitor1')
        tof_monitor1 = facility('tof_monitor1', default = 'tof_monitor1')

        #neutron recorder
        neutron_recorder = facility(
            'neutron_recorder', default = 'neutron_recorder')

        pass # end of Inventory


    def _defaults(self):
        
        base._defaults(self)
        
        self.inventory.sequence = [
            
            'moderator',
            'core_vessel_insert',
            'shutter_guide',
            'guide1',
            
            't0_chopper',
            
            'guide2',
            
            'fermi_chopper',
            
            'guide3', 'guide4', 'guide5',
            
            'energy_monitor1', 'tof_monitor1',

            'neutron_recorder',
            ]
        
        geometer = self.inventory.geometer
        geometer.inventory.moderator = (0,0,0), (0,0,0)
        geometer.inventory.core_vessel_insert = (0,0,1.), (0,0,0)
        geometer.inventory.shutter_guide = (0,0, 2.2679), (0,0,0)
        geometer.inventory.guide1 = (0,0,4.179), (0,0,0)
        geometer.inventory.t0_chopper = (0,0,9.000), (0,0,0)
        geometer.inventory.guide2 =  (0,0,9.482), (0,0,0)
        geometer.inventory.fermi_chopper = (0,0,11.6), (0,0,0)
        geometer.inventory.guide3 = (0,0,11.815), (0,0,0)
        geometer.inventory.guide4 = (0,0,12.061), (0,0,0)
        geometer.inventory.guide5 = (0,0,13.017), (0,0,0)
        geometer.inventory.energy_monitor1 = (0,0,13.407), (0,0,0)
        geometer.inventory.tof_monitor1 = (0,0,13.407), (0,0,0)
        geometer.inventory.neutron_recorder = (0,0,13.45), (0,0,0)
        return


if __name__ == '__main__' :
    instrument = Moderator2Sample('ARCS_Moderator2Sample')
    instrument.run()
        

# version
__id__ = "$Id$"

#  End of file 
