#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.inventory.properties.List import List as base
class List(base):

    def _cast(self,text):
        try: ret = eval(text)
        except: ret = base._cast(self, text)
        if isinstance( ret, list ): return ret
        raise TypeError("property '%s': could not convert '%s' to a list" % (self.name, text))
    


# version
__id__ = "$Id$"

# End of file 
