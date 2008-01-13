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


from pyre.xml.Document import Document as DocumentNode


class Document(DocumentNode):


    tags = [
        "ScatteringKernel",
        
        'KernelContainer',

        'SQEkernel',
        'GridSQE',
        ]


    def onScatteringKernel(self, scatteringkernel):
        self.document = scatteringkernel
        return


# version
__id__ = "$Id: Document.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
