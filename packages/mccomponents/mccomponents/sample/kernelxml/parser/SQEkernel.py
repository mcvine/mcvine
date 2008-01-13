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


from AbstractNode import AbstractNode, debug


class SQEkernel(AbstractNode):


    tag = "SQEkernel"

    def elementFactory( self, **kwds ):
        Qrange = self._parse( kwds['Q-range'] )
        Erange = self._parse( kwds['energy-range'] )
        scatterer = self.document.scatterer

        #from mccomponents.homogeneous_scatterer.HomogeneousScatterer import HomogeneousScatterer
        #assert isinstance(scatterer, HomogeneousScatterer )

        from mccomponents.sample import sqekernel
        return sqekernel(
            Qrange = Qrange, Erange = Erange)


    def onSQE(self, sqe):
        self.element.SQE = sqe
        return


    onGridSQE = onSQE


    pass # end of SQEkernel


# version
__id__ = "$Id$"

# End of file 
