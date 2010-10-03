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


from mccomponents.homogeneous_scatterer.hsxml.Renderer import Renderer as base


class Renderer(base):


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
            '<SQEkernel energy-range="%s" Q-range="%s">' % (
            sqekernel.Erange, sqekernel.Erange,
            )
            )

        self._indent()
        sqekernel.SQE.identify(self)
        self._outdent()

        self._write('</SQEkernel>')
        return


    def onIsotropicKernel(self, kernel):
        self._write('<IsotropicKernel>')
        self._write('</IsotropicKernel>')
        return


    def onConstantEnergyTransferKernel(self, kernel):
        E = kernel.E
        self._write('<ConstantEnergyTransferKernel energy-transfer="%s">' % E)
        self._write('</ConstantEnergyTransferKernel>')
        return


    def onConstantQEKernel(self, kernel):
        E = kernel.E; Q = kernel.Q
        self._write('<ConstantQEKernel momentum-transfer="%s" energy-transfer="%s">' % (
                Q, E))
        self._write('</ConstantQEKernel>')
        return


    def onGridSQE(self, gridsqe):
        sqehist = gridsqe.sqehist
        from histogram.hdf import dump
        filename = 'sqehist.h5'
        h5path = 'S(Q,E)'
        dump(sqehist, filename, '/', 'c')
        self._write(
            '<GridSQE histogram-hdf-path="%s"/>' % '/'.join( [filename, h5path] )
            )
        return


    def onSQE_fromexpression(self, sqe_fromexpression):
        expr = sqe_fromexpression.expression
        self._write(
            '<SQE_fromexpression expression="%s"/>' % expr
            )
        return


    def __init__(self):
        base.__init__(self)
        return

    pass # end of Renderer



# version
__id__ = "$Id$"

# End of file 
