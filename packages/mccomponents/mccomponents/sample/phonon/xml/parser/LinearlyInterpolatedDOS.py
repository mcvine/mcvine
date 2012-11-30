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


class LinearlyInterpolatedDOS(AbstractNode):


    tag = "LinearlyInterpolatedDOS"


    def elementFactory( self, **kwds ):
        datapath = kwds.get('idf-data-path')
        if datapath:
            pass
        else:
            raise ValueError, "LinearlyInterpolatedDOS needs path to "\
                  "idf data files"
        
        from mccomponents.sample.phonon import dos_fromidf
        return dos_fromidf( datapath )

    pass # end of LinearlyInterpolatedDOS


# version
__id__ = "$Id: LinearlyInterpolatedDOS.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
