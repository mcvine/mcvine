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

class NotRegisteredError(Exception): pass

class Registry:


    def __init__(self):
        self.factories = {} # (category, type): factory
        self.infos = {} # (category, type): info
        self.types = {} # dictionary of category: type list 
        return


    def registered(self, category, type):
        key = category, type
        return key in self.factories


    def register(self, category, type, module):
        self._addType( category, type )
        key = category, type
        from ._proxies import createFactory
        self.factories[ key ] = createFactory(category, type, module)
        self.infos[ key ] = module.info
        return


    def getFactory(self, category, type ):
        factories = self.factories
        key = category, type
        if not factories.has_key( key ):
            self._importComponent( key )
        return factories[ key ]


    def getInfo(self, category, type):
        infos = self.infos
        key = category, type
        if not infos.has_key( key ):
            return self._importComponent( key ).info
        return infos[ key ]


    def importAllComponents(self):
        from repositories import all as repos
        repos = list(repos)
        
        for repo in repos:
            pkg = __import__(repo, {}, {}, [''])
            cats = self._listCategoriesInPythonPackage(pkg)
            map(self._importComponentsInCategory, cats)
            continue
        return


    def _listCategoriesInPythonPackage(self, pkg):
        pkgpath = os.path.abspath(pkg.__path__[0])
        entries = os.listdir(pkgpath)

        for e in entries:
            p = os.path.join(pkgpath, e)
            if not os.path.isdir(p):
                continue
            if e.find('.')!=-1:
                raise NotImplementedError, str(e)
            initpy = os.path.join(p, '__init__.py')
            if not os.path.exists(initpy):
                continue
            m = '%s.%s' % (pkg.__name__, e)
            yield __import__(m, {}, {}, [''])
            continue
        return


    def _importComponentsInCategory(self, category):
        categorypath = os.path.abspath(category.__path__[0])
        categoryname = category.__name__
        entries = os.listdir(categorypath)
        imported = []
        pyexts = ['.py', '.pyc', '.pyo']
        from mcni.AbstractComponent import AbstractComponent
        for e in entries:
            base, ext = os.path.splitext(e)
            if ext not in pyexts:
                continue
            if base in imported:
                continue
            
            type = base
            modulename = '%s.%s' % (categoryname, type )
            try:
                module = __import__( modulename, {}, {}, [''] )
            except:
                continue

            if getattr(module, 'factory', None) is None:
                continue
            
            imported.append(base)
            self.register(categoryname.split('.')[-1], type, module)
            continue
        return 

    
    def _importComponent( self, key ):
        from repositories import all as repos
        repos = list(repos)
        # look in the last repository first
        repos.reverse()
        
        category, type = key

        module = None
        for repo in repos:
            modulename = '%s.%s.%s' % (
                repo, category, type )
            try:
                module = __import__( modulename, {}, {}, [''] )
            except:
                continue
            break

        if module:
            self.register( category, type, module )
        else:
            raise NotRegisteredError, "component %r of category %r " % (type, category)
        
        return module


    def _addType( self, category, type ):
        assert isinstance( category, str )
        assert isinstance( type, str )
        types = self.types
        if category in types:
            if type in types[category]: return
            types[category].append( type )
            return
        else:
            types[category] = [type]
            return
        raise "Should not reach here. category=%s, type=%s" % (
            category, type)
    
    pass # end of Registry


import os


# version
__id__ = "$Id$"

# End of file 
