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


# the interface
from register_CompositeDetector import CompositeDetector as base
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


# dummy class
class Tof2Channel: pass

    
# 2. the handler to construct c++ engine
def onDetectorSystem(self, detectorSystem):
    #tof->channel converter
    tofmin, tofmax, tofstep = detectorSystem.tofparams
    t2c = self.factory.tof2channel(tofmin, tofmax, tofstep)

    #
    mca = detectorSystem.mca.identify(self)

    #attach to factory
    self.factory.binding.t2c = t2c
    self.factory.binding.mca = mca
    
    self._indexes_in_detsys = []
    ret = self.onCompositeDetector( detectorSystem )
    del self._indexes_in_detsys

    del self.factory.binding.t2c, self.factory.binding.mca
    return ret


def bp_tof2channel( self, tofmin, tofmax, tofstep ):
    import mccomponents.mccomponentsbp as b
    return b.Tof2Channel( tofmin, tofmax, tofstep )


# 4. register the new class and handlers
import mccomponents.homogeneous_scatterer as mh
mh.register_engine_ctor (DetectorSystem, onDetectorSystem )
mh.register_binding_handlers(
    Tof2Channel,
    { 'BoostPythonBinding': bp_tof2channel }
    )


# version
__id__ = "$Id$"

# End of file 
