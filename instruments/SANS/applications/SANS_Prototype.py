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


from SSSD import Instrument as base
class SANS_Prototype(base):

    class Inventory(base.Inventory):
        
        pass # end of Inventory


    def _defaults(self):
        
        base._defaults(self)
        
        geometer = self.inventory.geometer
        geometer.inventory.source = (0,0,0), (0,0,0)
        geometer.inventory.sample = (0,0,16), (0,0,0)
        geometer.inventory.neutron_recorder = (0,0,16), (0,0,0)
        geometer.inventory.detector = (0,0,26), (0,0,0)
        return
    

    def __init__(self, name = "SANS_Prototype"):
        base.__init__(self, name)
        return


    pass # end of Test


def main():
    import journal
    app = SANS_Prototype()
    return app.run()


if __name__ == '__main__' : main()

    
# version
__id__ = "$Id$"

#  End of file 
