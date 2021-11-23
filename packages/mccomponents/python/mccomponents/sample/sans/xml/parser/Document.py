#!/usr/bin/env python
#
#

from mccomponents.sample.kernelxml.parser import getDocument, updateDocument
base = getDocument()

class Document(base):

    tags = [
        'SANSSpheresKernel',
        ]

    pass # end of Document

updateDocument( Document )

# End of file
