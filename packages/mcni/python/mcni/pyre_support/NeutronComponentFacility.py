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


    def __init__(self, name, family=None, **kwds):
        family = family or 'neutroncomponent'
        super(NeutronComponentFacility, self).__init__(name, family, **kwds)
        return


    def _import(self, name):
        component, locator = self._createNeutronComponent(name)
        if component is None:
            return super(NeutronComponentFacility, self)._import(name)
        return component, locator


    def _retrieveComponent(self, instance, componentName, args):
        # try to load using my name first
        component = instance.retrieveComponent(name=componentName, factory=self.name, args=args)
        if component is not None:
            # if successful, we are good
            locator = component.getLocator()
            # adjust the names by which this component is known
            component.aliases.append(self.name)
            return component, locator
        
        # the original implementation in my ancestor pyre.inventory.Facility
        # will load using my family name
        return super(NeutronComponentFacility, self)._retrieveComponent(
            instance, componentName, args)


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
         * <supplier>://<componentcategory>/<componenttypefactory>(*args)
           eg. mcni://sources/NDMonitor(x, y)
        '''
        component_specifier = str(component_specifier)
        supplier, category, type, args = _decode(component_specifier)
        
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

        # component type factory ?
        if args:
            factory = factory(*args)
        
        # instantiate the component
        component = factory(self.name)

        # uri
        uri = _encode(factory.supplier, factory.category, factory.type, args)
        component.uri = uri
        # locator
        locator = '<mcvine.componentfactory>'
        #
        return component, locator


    def _set(self, instance, component, locator):
        if isinstance(component, str):
            # bypass the standard pyre component specification syntax
            # of component:args. only use the "component" part. the 
            # args part is handled in _import 
            name = component
            args = []
            component, source = self._retrieveComponent(instance, name, args)

            import pyre.parsing.locators
            locator = pyre.parsing.locators.chain(source, locator)

        # all the following are just copied from pyre.inventory.Facility
        if component is None:
            return

        # get the old component
        try:
            old = instance._getTraitValue(self.name)
        except KeyError:
            # the binding was uninitialized
            return instance._initializeTraitValue(self.name, component, locator)

        # if the previous binding was non-null, finalize it
        if old:
            old.fini()
        
        # bind the new value
        return instance._setTraitValue(self.name, component, locator)
    
    
    pass # end of NeutronComponentFacility


def _encode(supplier, category, type, args):
    if args:
        argsstr = ','.join(args)
        argsstr = '(' + argsstr + ')'
    else:
        argsstr = ''
    # XXX: don't really need supplier and category right now.
    # XXX: rethink this again later
    # return '%s://%s/%s%s' % (supplier, category, type, argsstr)
    return '%s/%s%s' % (category, type, argsstr)


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
        argsstr = ''
    else:
        type, argsstr = t2.strip()[:-1].split('(')

    args = None
    argsstr = argsstr.strip()
    if argsstr:
        args = argsstr.split(',')
        args = [a.strip() for a in args]
    return supplier, category, type, args


def test_decode():
    assert _decode('MonochromaticSource') == (None, None, 'MonochromaticSource', None)
    assert _decode('sources/MonochromaticSource') == (None, 'sources', 'MonochromaticSource', None)
    assert _decode('mcni://MonochromaticSource') == ('mcni', None, 'MonochromaticSource', None)
    assert _decode('mcni://sources/MonochromaticSource') == ('mcni', 'sources', 'MonochromaticSource', None)
    assert _decode('mcni://sources/NDMonitor(x, y)') == ('mcni', 'sources', 'NDMonitor', ['x', 'y'])
    return


def main():
    test_decode()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
