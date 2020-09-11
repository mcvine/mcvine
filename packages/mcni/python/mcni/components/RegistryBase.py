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

class RegistryBase:


    def __init__(self):
        self.factories = {} # (category, type): factory
        self.types = {} # dictionary of category: type list
        self.setup_repos()
        return


    def listallcomponentcategories(self):
        components = self.listallcomponents()
        ret = [ category for category, type in components ]
        return uniquelist( ret )


    def listcomponentsincategory(self, category):
        components = self.listallcomponents()
        components = [component for component in components if component[0] == category]
        return [ type for category, type in components ]


    def listallcomponents(self):
        '''return a list of (category, type) tuples
        '''
        static_components = self._getStaticComponentList( )
        dynamic_components = list(self.factories.keys())
        return uniquelist( static_components + dynamic_components )
    

    def setup_repos(self):
        raise NotImplementedError


    def registered(self, category, type):
        key = category, type
        return key in self.factories


    def register(self, category, type, factory):
        self._addType( category, type )
        key = category, type
        self.factories[ key ] = factory
        return


    def getFactory(self, category, type ):
        factories = self.factories
        key = category, type
        if key not in factories:
            return self._getStaticComponent( key )
        return factories[ key ]


    def getInfo(self, category, type):
        return self.getFactory( category, type ).__doc__


    def _getStaticComponentList(self):
        '''return a list of (category, type) tuples.
        both category and type are strings.
        '''
        ret = []
        for repo in self.repos:
            debug.log('working on repo %s' % (repo,))
            package = __import__( repo, {}, {}, [''] )
            path = os.path.dirname( package.__file__ )
            
            files = os.listdir( path )
            debug.log('files:: %s' % (files,))
            for f in files:
                modulename = os.path.splitext( f )[0]
                m = __import__( '%s.%s' % (repo, modulename), {}, {}, ['']  )
                try: category = getattr(m, 'category')
                except:
                    continue
                type = modulename
                signature = category, modulename
                if signature not in ret: ret.append( signature )
                continue
            continue
        return ret
                
    
    def _getStaticComponent( self, key ):
        repos = self.repos
        
        category, type = key

        module = None
        for repo in repos:
            modulename = '%s.%s' % (
                repo, type )
            try:
                module = __import__( modulename, {}, {}, [''] )
            except ImportError:
                continue

        if module:
            if category != module.category :
                raise RuntimeError("component %r is a %r, not a %r" % (
                    type, module.category, category ))
            factory = getattr(module, type)
            self.register( category, type, factory )
        else:
            raise NotRegisteredError("component %r of category %r " % (
                type, category ))
        
        return factory


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
        raise RuntimeError("Should not reach here")
    
    pass # end of Registry


from mcni.utils import uniquelist
import os

import journal
debug = journal.debug('mcni.components.Registry')


# version
__id__ = "$Id$"

# End of file 
