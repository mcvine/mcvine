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


from mccomponents.detector.ComputationEngineRendererExtension import register, ComputationEngineRendererExtension


#Detector actually means he3 tube. we should use more specific name
#but right now instrument package still use "Detector", so we have
#to have this available.
class Detector: pass
register(Detector, ComputationEngineRendererExtension.onHe3Tube )
class DetectorCopy: pass
register(DetectorCopy, ComputationEngineRendererExtension.onHe3TubeCopy )



# version
__id__ = "$Id$"

# End of file 
