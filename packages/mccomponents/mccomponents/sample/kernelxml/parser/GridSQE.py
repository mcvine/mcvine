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


class GridSQE(AbstractNode):


    tag = "GridSQE"

    def elementFactory( self, **kwds ):
        datapath = kwds['data-path']
        from mccomponents.sample.idf import readSQE
        sqe = readSQE( datapath )
        from mccomponents.sample import gridsqe, sqekernel
        return sqekernel( gridsqe( sqe ) )

    pass # end of GridSQE


# version
__id__ = "$Id$"

# End of file 
