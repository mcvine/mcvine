#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from mcni.pyre_support.Instrument import Instrument as base
class Instrument(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility
        source = facility(name='source')
        monitor = facility(name='monitor')
        pass # end of Inventory


    def __init__(self, name = 'componentfactory_deomoapp'):
        base.__init__(self, name)
        return
    

    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'monitor']

        from mcstas2.pyre_support import componentfactory as factory
        self.inventory.source = factory('sources', 'Source_simple')('source')
        self.inventory.monitor = factory('monitors', 'E_monitor')('monitor')

        # print self.inventory.source
        
        geometer = self.inventory.geometer

        geometer.inventory.monitor = (0,0,1), (0,0,0)

        return
    
    pass # end of Instrument



if __name__ == "__main__": 
    instr = Instrument()
    instr.run()
    instr.run_postprocessing()
    
# End of file 
