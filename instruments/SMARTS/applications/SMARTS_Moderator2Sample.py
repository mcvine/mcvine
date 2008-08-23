#! /usr/bin/env python
#
###############################################################################
#                            Iowa State University
#                        Ersan Ustundag Research Group
#                 DANSE Project Engineering Diffraction Subgroup
#                    Copyright (c) 2007 All rights reserved.
#                              Coded by: Li Li 
###############################################################################



from mcni.pyre_support.Instrument import Instrument as base
class Moderator2Sample(base):

    class Inventory(base.Inventory):
        
        from mcni.pyre_support import facility
        source = facility('source', default = 'source')
        guide1 = facility('guide1', default = 'guide1')
        guide2 = facility('guide2', default = 'guide2')
        slit1 = facility('slit1', default = 'slit1')
        slit2 = facility('slit2', default = 'slit2')

        #neutron recorder
        neutron_recorder = facility(
            'neutron_recorder', default = 'neutron_recorder')

        
        pass # end of Inventory


    def _defaults(self):
        
        base._defaults(self)
        
        self.inventory.sequence = [            
            'source',
            'guide1',
            'guide2',
            'slit1',
            'slit2',
            'neutron_recorder',
            ]
        
        geometer = self.inventory.geometer
        geometer.inventory.source = (0,0,0), (0,0,0)
        geometer.inventory.guide2 = (0,0,5), (0,0,0)
        geometer.inventory.guide2 = (0,0,10), (0,0,0)
        geometer.inventory.slit1 = (0,0,29.0), (0,0,0)
        geometer.inventory.slit2 = (0,0,30.5), (0,0,0)
        geometer.inventory.neutron_recorder = (0,0,30.6), (0,0,0)
        return
    

    def __init__(self, name = "SMARTS_Moderator2Sample"):
        base.__init__(self, name)
        return


    pass # end of Test


def main():
    import journal
    app = Moderator2Sample()
    return app.run()


if __name__ == '__main__' : main()

    
# version
__id__ = "$Id$"

#  End of file 
