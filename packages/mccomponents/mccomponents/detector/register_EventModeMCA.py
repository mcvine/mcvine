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


class EventModeMCA:

    def __init__(self, outfilename, detectorDims ):
        '''event mode multi channel analyzer

        outfilename: output data file name
        detectorDims: dimensions of detector system.
          For example, a detector system of 100 packs, 8 tubes per pack, 100 pixels per tube:
            detectorDims = 100, 8, 100
        '''

        self.outfilename = outfilename
        self.detectorDims = detectorDims
        return

    def identify(self, visitor):
        return visitor.onEventModeMCA(self)

    pass # end of EventModeMCA


# 2. the handler to construct c++ engine
def onEventModeMCA(self, mca):
    return self.factory.eventmodemca( mca.outfilename, mca.detectorDims )


def bp_eventmodemca( self, outfilename, detectorDims ):
    import mccomponents.mccomponentsbp as b
    dims = b.vector_uint( 0 )
    for dim in detectorDims: dims.append(dim)
    return b.EventModeMCA( outfilename, dims )



# 4. register the new class and handlers
import mccomponents.homogeneous_scatterer as mh
mh.register(EventModeMCA, onEventModeMCA,
            {'BoostPythonBinding': bp_eventmodemca})

    
# version
__id__ = "$Id$"

# End of file 
