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


def extendDocument( new ):
    global _Document
    _Document = new
    return


def document_class():
    return _Document


from Document import Document as _Document


# version
__id__ = "$Id: __init__.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
