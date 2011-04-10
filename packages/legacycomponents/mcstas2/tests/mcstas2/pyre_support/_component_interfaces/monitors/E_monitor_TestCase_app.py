#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



# test instrument
from TestInstrument1 import Instrument as base
class Instrument(base):

    def __init__(self, name='E_monitor_TestCase'):
        base.__init__(self, name)
        return
    

if __name__ == "__main__":
    Instrument('E_monitor_TestCase').run()

    
# version
__id__ = "$Id: E_monitor_TestCase_app2.py 862 2011-02-10 20:17:46Z linjiao $"

# End of file 
