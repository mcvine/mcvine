# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def store( path ):
    store = _stores.get(path)
    if store is None:
        store = _stores[path] = PacketSizeStore( path )
    return store
_stores = {}


class PacketSizeStore:

    def __init__(self, path):
        self.path = path
        import os
        if os.path.exists( path ):
            self.handle = open(path, 'r')
        else:
            self.handle = open(path, 'w+')
        self.size = None
        return


    def getsize(self):
        if self.size is None:
            text = self.handle.read()
            if len(text) == 0: return 
            size = long( text )
            self.size = size
        return self.size


    def setsize(self, size):
        if self.size  and  size != self.size: raise RuntimeError, "packet size cannot be changed"
        if size <= 0: raise ValueError, "packet size must be positive: size=%s" % size
        if self._check_size_type(size): raise TypeError, "packet size must be an integer"
        self.handle.write( '%s'% size )
        self.size = size
        return size
    

    def _check_size_type(self, size):
        types = [int, long]
        for type in types:
            if isinstance( size, type): return False
            continue
        return True


# version
__id__ = "$Id$"

# End of file 
