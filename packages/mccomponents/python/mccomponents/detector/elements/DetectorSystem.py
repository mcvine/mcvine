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


from .CompositeDetector import CompositeDetector as base

class DetectorSystem(base):

    def __init__(self, shape, tofparams, mca = None):
        '''
        tofparams: tofmin, tofmax, tofstep
        mca: multichannel analyzer
        '''
        base.__init__(self, shape)
        self.tofparams = tofparams
        self.mca = mca
        return

    def identify(self, visitor): return visitor.onDetectorSystem(self)
    
    pass


# version
__id__ = "$Id$"

# End of file 
