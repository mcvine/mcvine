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


from pyre.inventory.Facility import Facility


class NeutronComponentFacility( Facility ):


    def _import(self, name):
        component, locator = self._createNeutronComponent(name)
        if component is None:
            return super(NeutronComponentFacility, self)._import(name)
        return component, locator

            
    def _createNeutronComponent(self, component_specifier):
        '''create a pyre neutron component from the given name
        
        the name could be
         * <componenttype>
           eg. MonochromaticSource
         * <componentcategory>/<componenttype>
           eg. sources/MonochromaticSource
         * <supplier>://<componenttype>
           eg. mcni://MonochromaticSource
         * <supplier>://<componentcategory>/<componenttype>
           eg. mcni://sources/MonochromaticSource
         * <supplier>://<componentcategory>/<componenttype>(<componentname>)
           eg. mcni://sources/MonochromaticSource(source)
        '''
        component_specifier = str(component_specifier)
        supplier, category, type, name = _decode(component_specifier)
        
        # component factory
        from mcni.pyre_support import findcomponentfactory
        try:
            factory = findcomponentfactory(type, category, supplier)
        except:
            import journal, traceback
            tb = traceback.format_exc()
            journal.error('pyre.inventory').log('failed to find component factory %r. \n%s' % (
                    component_specifier, tb))
            return None, None
        
        # error handling
        if not factory:
            import journal
            journal.error("mcvine.component").log(
                "could not bind facility '%s': component factory '%s' not found." % (
                self.name, component_specifier)
                )
            return None, None
        
        # instantiate
        if not name: name = self.name
        uri = _encode(factory.supplier, factory.category, factory.type, name)
        # XXX: the above does not work. pyre does not like abc://d.e/...
        # XXX: for now, just <category>/<type>
        uri = '%s/%s' % (factory.category, factory.type)
        component = factory(name)
        component.uri = uri
        # locator
        locator = '<mcvine.componentfactory>'
        #
        return component, locator

    pass # end of NeutronComponentFacility


def _encode(supplier, category, type, name):
    return '%s://%s/%s(%s)' % (supplier, category, type, name)


def _decode(specifier):
    if specifier.find('://') == -1:
        supplier = None
        t1 = specifier
    else:
        supplier, t1 = specifier.split('://')

    if t1.find('/') == -1:
        t2 = t1
        category = None
    else:
        category, t2 = t1.split('/')
    
    if t2.find('(') == -1:
        type = t2
        name = None
    else:
        type, name = t2.strip()[:-1].split('(')
    return supplier, category, type, name


def test_decode():
    assert _decode('MonochromaticSource') == (None, None, 'MonochromaticSource', None)
    assert _decode('sources/MonochromaticSource') == (None, 'sources', 'MonochromaticSource', None)
    assert _decode('mcni://MonochromaticSource') == ('mcni', None, 'MonochromaticSource', None)
    assert _decode('mcni://sources/MonochromaticSource') == ('mcni', 'sources', 'MonochromaticSource', None)
    assert _decode('mcni://sources/MonochromaticSource(source)') == ('mcni', 'sources', 'MonochromaticSource', 'source')
    return


def main():
    test_decode()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
