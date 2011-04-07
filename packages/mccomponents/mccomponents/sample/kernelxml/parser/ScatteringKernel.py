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


from pyre.xml.Node import Node


class ScatteringKernel(Node):


    tag = "ScatteringKernel"
    
    def __init__(self, document, attributes):
        Node.__init__(self, document)
        return


    def notify(self, parent):
        #parent is the Document node. document.scatterer is a scatterer instance
        #that this kernel should be attached to
        target = parent.scatterer
        target.setKernel( self._kernel )
        parent.document = self._kernel
        return


    def on_(self, sth):
        self._kernel = sth
        return

    onKernelContainer = onSQEkernel = onIsotropicKernel \
        = onE_Q_Kernel \
        = onConstantEnergyTransferKernel = onConstantQEKernel \
        = on_
    
    pass # end of ScatteringKernel
    


# version
__id__ = "$Id$"

# End of file 
