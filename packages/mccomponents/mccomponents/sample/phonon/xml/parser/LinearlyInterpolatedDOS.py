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
        idfpath = kwds.get('idf-data-path')
        h5path = kwds.get('histogram-path')
        asciipath = kwds.get('ascii-path')
        
        if idfpath:
            from mccomponents.sample.phonon import dos_fromidf
            return dos_fromidf(idfpath)
        elif h5path:
            from mccomponents.sample.phonon import dos_fromh5
            return dos_fromh5(h5path)
        elif asciipath:
            from mccomponents.sample.phonon import dos_fromascii
            return dos_fromascii(h5path)
        else:
            raise ValueError, "LinearlyInterpolatedDOS needs path to "\
                "idf or histogram data file"            
        
    pass # end of LinearlyInterpolatedDOS


# version
__id__ = "$Id: LinearlyInterpolatedDOS.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
