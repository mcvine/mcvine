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


from mccomponents.sample.kernelxml.parser import getDocument, updateDocument
base = getDocument()


class Document(base):


    tags = [
        'Phonon_CoherentInelastic_PolyXtal_Kernel',
        'LinearlyInterpolatedDispersion',
        ]


    pass # end of Document


updateDocument( Document )


# version
__id__ = "$Id$"

# End of file 
