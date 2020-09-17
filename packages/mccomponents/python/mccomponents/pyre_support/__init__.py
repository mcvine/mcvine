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


def _register_components():
    from mcni.pyre_components import registercomponent

    from .components.SampleAssemblyFromXml import SampleAssemblyFromXml
    registercomponent( 'samples', 'SampleAssemblyFromXml', SampleAssemblyFromXml )

    from .components.DetectorSystemFromXml import DetectorSystemFromXml
    registercomponent( 'detectors', 'DetectorSystemFromXml', DetectorSystemFromXml )
    return


_register_components()


# version
__id__ = "$Id$"

# End of file 
