#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


#from pyre.xml.Document import Document as DocumentNode
from instrument.geometry.pml.parser.Document import Document as base


class Document(base):


    tags = [
        "HomogeneousScatterer",
        'CompositeKernel',
        'InverseVelocityAbsorption',
        'InterpolateAbsorptionFromCurve',
        ]


    def onHomogeneousScatterer(self, homogeneous_scatterer):
        self.document = homogeneous_scatterer
        return


# version
__id__ = "$Id$"

# End of file 
