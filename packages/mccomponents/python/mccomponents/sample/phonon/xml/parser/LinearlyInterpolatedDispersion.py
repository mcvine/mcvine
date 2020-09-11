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


from .AbstractNode import AbstractNode, debug


class LinearlyInterpolatedDispersion(AbstractNode):


    tag = "LinearlyInterpolatedDispersion"


    def elementFactory( self, **kwds ):
        datapath = kwds.get('idf-data-path')
        if datapath:
            pass
        else:
            raise ValueError("LinearlyInterpolatedDispersion needs path to "\
                  "idf data files")
        
        from mccomponents.sample.phonon import periodicdispersion_fromidf
        return periodicdispersion_fromidf( datapath )

    pass # end of LinearlyInterpolatedDispersion


# version
__id__ = "$Id$"

# End of file 
