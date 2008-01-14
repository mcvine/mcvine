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


#from pyre.weaver.mills.XMLMill import XMLMill
from instrument.geometry.pml.Renderer import Renderer as base


class Renderer(base):


    def render(self, kernel):
        document = self.weave(kernel)
        return document


    # handlers

    def onCompositeKernel(self, compositekernel):
        self._write('')
        self._write('<compositekernel>')
        self._indent()
        for kernel in compositekernel.elements():
            kernel.identify(self)
            continue
        self._outdent()
        self._write('</compositekernel>')
        self._write('')
        return


    def onHomogeneousScatterer(self, hs):
        self._write('')
        mcweights = hs.mcweights_absorption_scattering_transmission
        self._write('<homogeneous_scatterer mcweights="%s">' % mcweights )
        self._indent()

        hs.shape().identify(self)
        hs.kernel().identify(self)
        
        self._outdent()
        self._write('</homogeneous_scatterer>' )
        self._write( '' )
        return


    def __init__(self):
        base.__init__(self)
        return


    def _renderDocument(self, document):
        self._rep += ['', '<!DOCTYPE homogeneous_scatterer>', '']

        document.identify(self)
        return

    pass # end of Renderer



# version
__id__ = "$Id: Renderer.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
