#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

import os
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'

skip = False
standalone = True

import unittestX as unittest


#
from mcni.pyre_support.AbstractComponent import AbstractComponent
class Validator(AbstractComponent):
    
    def process(self, neutrons):
        # print self.name
        for n in neutrons:
            # print n
            assert n.state.position[2] == 0
        return neutrons


# test instrument
from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        from mcstas2.pyre_support import facility
        source = facility( 'sources', 'Source_simple', 'source' )
        validator1 = facility( 'monitors', 'E_monitor', 'validator1') 
        monitor = facility( 'monitors', 'E_monitor', 'monitor') 
        validator2 = facility( 'monitors', 'E_monitor', 'validator2') 
        pass # end of Inventory


    def __init__(self, name='restore_neutrons_TestCase'):
        base.__init__(self, name)
        return


    def _defaults(self):
        base._defaults(self)

        self.inventory.sequence = [
            'source', 'validator1', 'monitor', 'validator2']
        self.inventory.outputdir = 'restore_neutrons_TestCase-out'
        self.inventory.ncount = 5
        self.inventory.buffer_size = 5
        self.inventory.overwrite_datafiles = 1

        geometer = self.inventory.geometer
        geometer.inventory.monitor = (0,0,1), (0,0,0)
        
        monitor = self.inventory.monitor
        monitor.inventory.restore_neutron = 1

        self.inventory.validator1 = Validator('validator1', 'validator')
        self.inventory.validator2 = Validator('validator2', 'validator')
        return
    

    pass # end of Instrument
    

class TestCase(unittest.TestCase):

    def test1(self):
        instrument = Instrument()
        instrument.run()
        instrument.run_postprocessing()
        return
    
    pass  # end of TestCase


import os

if __name__ == "__main__": unittest.main()
    
# End of file 
