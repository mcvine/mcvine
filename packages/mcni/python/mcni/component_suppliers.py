#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
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


class Supplier(object):

    def listallcomponentcategories(self):
        raise NotImplementedError

    def listcomponentsincategory(self, category):
        raise NotImplementedError

    def componentfactory(self, category, type):
        raise NotImplementedError

    def componentinfo(self, category, type):
        raise NotImplementedError

    pass # end of Supplier



class PyModuleAsSupplier(Supplier):


    def __init__(self, pymodulename):
        self.pymodulename = pymodulename
        return

    def __getattribute__(self, name):
        if name == 'pymodulename': return object.__getattribute__(self, name)
        m = __import__(self.pymodulename, {}, {}, [''] )
        return getattr(m, name)

    


_all = {}

_all['mcni'] = PyModuleAsSupplier( 'mcni.components' )
# _all['mcstas2'] = PyModuleAsSupplier( 'mcstas2' )


# version
__id__ = "$Id$"

#  End of file 
