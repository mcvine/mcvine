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


## This package contains homogeneous scatterers that can
## be modeled as a shape and a scattering kernel.



def srandom( seed ):
    from homogeneous_scatterer import srandom
    return srandom( seed )
from mcni.seeder import register
register( srandom )
del register


def _register_components():
    from mcni.components import registercomponent
    
    from sample import samplecomponent
    registercomponent( 'samples', 'SampleAssemblyFromXml', samplecomponent )

    from detector import detectorcomponent
    registercomponent( 'detectors', 'DetectorSystemFromXml', detectorcomponent )
    return



_register_components()




# version
__id__ = "$Id$"


# End of file 
