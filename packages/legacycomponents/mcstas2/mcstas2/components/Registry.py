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

class Registry:


    def __init__(self):
        self.memory = {}
        return


    def register(self, category, type, factory):
        self.memory[ (category, type) ] = factory
        return


    def get(self, category, type ):
        memory = self.memory
        key = category, type
        if not memory.has_key( key ):
            return self._getStaticComponent( key )
        return memory[ key ]

    
    def _getStaticComponent( self, key ):
        category, type = key
        modulename = 'mcstas2.components.%s.%s' % (
            category, type )
        try:
            module = __import__( modulename, {}, {}, [''] )
        except:
            raise "component %r of category %r does not exist"

        return module.factory
    
    pass # end of Registry



# version
__id__ = "$Id$"

# End of file 
