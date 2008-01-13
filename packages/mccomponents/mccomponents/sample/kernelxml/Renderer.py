#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                      California Institute of Technology
#                      (C)    2007   All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.weaver.mills.XMLMill import XMLMill


class Renderer(XMLMill):


    def render(self, kernel):
        document = self.weave(kernel)
        return document


    # handlers

    def onKernelContainer(self, kernelContainer):
        self._write('')
        self._write('<kernelcontainer>')
        self._indent()
        for kernel in kernelContainer.elements():
            kernel.identify(self)
            continue
        self._outdent()
        self._write('</kernelcontainer>')
        self._write('')
        return


    def onSQEkernel(self, sqekernel):

        self._write(
            '<SQEkernel energy-range="%s" Q-range="%s">' )

        self._indent()
        sqekernel.SQE.identify(self)
        self._outdent()

        self._write('</SQEkernel>')
        return


    def __init__(self):
        XMLMill.__init__(self)
        return


    def _renderDocument(self, document):
        self._rep += ['', '<!DOCTYPE kernel>', '']

        self._rep += ['<ScatteringKernel>']
        document.identify(self)
        self._rep += ['</ScatteringKernel>']
        return

    pass # end of Renderer



# version
__id__ = "$Id: Renderer.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
