#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                 Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


def register( name, supplier ):
    global _all
    _all[ name ] = supplier
    return


def get(name):
    global _all
    return _all.get(name)


def all():
    global _all
    return _all


class SupplierMissing( Exception ): pass


class Supplier(object):

    def __getattribute__(self, name):
        raise NotImplementedError



class PyModuleAsSupplier(Supplier):


    def __init__(self, pymodulename):
        self.pymodulename = pymodulename
        return

    def __getattribute__(self, name):
        if name == 'pymodulename': return object.__getattribute__(self, name)
        try:
            m = __import__(self.pymodulename, {}, {}, [''] )
        except ImportError :
            raise SupplierMissing, "%s" % (self.pymodulename,)
        return getattr(m, name)

    


_all = {}

_all['mcni'] = PyModuleAsSupplier( 'mcni.pyre_components' )
# _all['mcstas2'] = PyModuleAsSupplier( 'mcstas2.pyre_support' )


# version
__id__ = "$Id$"

#  End of file 
