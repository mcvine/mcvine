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


    def onSQkernel(self, sqkernel):

        self._write(
            '<SQkernel Q-range="%s">' % (
            sqkernel.Erange,
            )
            )

        self._indent()
        sqkernel.SQ.identify(self)
        self._outdent()

        self._write('</SQkernel>')
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


    def onE_Q_Kernel(self, kernel):
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q
        Qmin = kernel.Qmin
        Qmax = kernel.Qmax
        self._write('<E_Q_Kernel E_Q="%s" S_Q="%s" Qmin="%s" Qmax="%s">' % (
                E_Q, S_Q, Qmin, Qmax))
        self._write('</E_Q_Kernel>')
        return


    def onBroadened_E_Q_Kernel(self, kernel):
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q
        sigma_Q = kernel.sigma_Q
        Qmin = kernel.Qmin
        Qmax = kernel.Qmax
        self._write('<Broadened_E_Q_Kernel E_Q="%s" S_Q="%s" sigma_Q="%s" Qmin="%s" Qmax="%s">' % (
                E_Q, S_Q, sigma_Q, Qmin, Qmax))
        self._write('</Broadened_E_Q_Kernel>')
        return
    
    
    def onE_Q_vKernel(self, kernel):
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q
        Emax = kernel.Emax
        self._write('<E_Q_Kernel E_Q="%s" S_Q="%s" Emax="%s">' % (
                E_Q, S_Q, Emax))
        self._write('</E_Q_Kernel>')
        return


    def onConstantQEKernel(self, kernel):
        E = kernel.E; Q = kernel.Q
        self._write('<ConstantQEKernel momentum-transfer="%s" energy-transfer="%s">' % (
                Q, E))
        self._write('</ConstantQEKernel>')
        return
    
    
    def onConstantvQEKernel(self, kernel):
        E = kernel.E; Q = kernel.Q
        dE = kernel.dE
        self._write('<ConstantvQEKernel momentum-transfer="%s" energy-transfer="%s" dE="%s">' % (
                Q, E, dE))
        self._write('</ConstantvQEKernel>')
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


    def onGridSQ(self, gridsq):
        sqhist = gridsq.sqhist
        from histogram.hdf import dump
        filename = 'sqhist.h5'
        h5path = 'S(Q)'
        dump(sqhist, filename, '/', 'c')
        self._write(
            '<GridSQ histogram-hdf-path="%s"/>' % '/'.join( [filename, h5path] )
            )
        return


    def onSQ_fromexpression(self, sq_fromexpression):
        expr = sq_fromexpression.expression
        self._write(
            '<SQ_fromexpression expression="%s"/>' % expr
            )
        return


    def __init__(self):
        base.__init__(self)
        return

    pass # end of Renderer



# version
__id__ = "$Id$"

# End of file 
