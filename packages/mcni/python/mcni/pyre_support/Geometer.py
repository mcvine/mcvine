#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component
class DefaultTransformer(Component):

    def __init__(self, name='coordinate-system-transformer', facility='transformer'):
        super(DefaultTransformer, self).__init__(name, facility)
        return
    
    def __call__(self, *args, **kwds):
        from mcni.coordinate_system_transformers.mcstas import transformCoordinateSystem
        return transformCoordinateSystem(*args, **kwds)



from pyre.inventory.Property import Property

class Register(Property):


    def __init__(self, name, default=None, meta=None, validator=None):
        if default is None:
            default = default_record
            
        Property.__init__(self, name, "geometer-record", default, meta, validator)
        return


    def _cast(self, value):
        # examples of good values:
        if isinstance(value, str):
            env = {'relative': RelativeCoord}
            value = eval(value, env)
            pass
        
        try:
            n = len(value)
        except:
            raise ValueError("%s. Should be a 2-tuple. Good examples: %s" % (
                value, good_records))

        if n != 2:
            raise ValueError("%s. Should be a 2-tuple. Good examples: %s" % (
                value, good_records))

        pos, ori = value
        pos = _toCoord(pos)
        ori = _toCoord(ori)
        
        return pos, ori


good_records = """
  * (0,0,3), (0,0,0)
  * (0,0,3), relative((0,0,90), to='previous')
  * relative((0,0,3), to='sample'), (0,0,0)
"""

from mcni.Geometer2 import _toCoord, Geometer as base, AbsoluteCoord, RelativeCoord
default_record = AbsoluteCoord((0,0,0)), AbsoluteCoord((0,0,0))
    

class Geometer(Component, base):

    # a weak reference to the instrument
    # will need it to support "previous" 
    instrument = None 

    
    class Inventory(Component.Inventory):

        import pyre.inventory
        transformer = pyre.inventory.facility('transformer', factory=DefaultTransformer)
        transformer.meta['tip'] = 'coordinate system transformer'

        dump = pyre.inventory.bool('dump')


    def __init__(self, name = 'geometer'):
        Component.__init__(self, name, 'geometer')
        base.__init__(self)

        import journal
        self._warning = journal.warning( 'mcni.pyre_support.geometer' )
        return


    def _get_comp_seq(self):
        seq = self.instrument.sequence
        return [getattr(self.instrument.inventory, n) for n in seq]
    element_sequence = property(_get_comp_seq)


    def _positionRecord(self, element):
        try:
            return base._positionRecord( self, element )
        except:
            try:
                return base._positionRecord( self, element.name )
            except:
                #end to try out all aliases
                aliases = getattr(element, 'aliases', None)
                if aliases is None:
                    raise RuntimeError('failed to find %r' % (element, ))
                
                for alias in element.aliases:
                    try: return base._positionRecord( self, alias )
                    except: pass
                    continue
                #still nothing
                raise "Position of element %s not registered" % element.name


    def _orientationRecord(self, element):
        try:
            return base._orientationRecord( self, element )
        except:
            try:
                return base._orientationRecord( self, element.name )
            except:
                aliases = getattr(element, 'aliases', None)
                if aliases is None:
                    raise RuntimeError('failed to find %r' % (element, ))

                #end to try out all aliases
                for alias in element.aliases:
                    try: return base._orientationRecord( self, alias )
                    except: pass
                    continue
                #still nothing
                raise "Orientation of element %s not registered" % element.name


    def _findReference(self, ref, element):
        if ref == 'previous':
            seq = self.element_sequence
            try:
                i = seq.index(element)
            except:
                seq = [c.name for c in seq]
                if not isinstance(element, str):
                    element = element.name
                i = seq.index(element)
            if i == 0:
                raise RuntimeError("there is no previous element for %s" % element)
            return seq[i-1]
        return ref
    

    def _configure(self):
        Component._configure(self)

        self.transformer = self.inventory.transformer
        
        for prop in self.inventory.propertyNames():
            v = self.inventory.getTrait( prop )
            if isinstance( v, Register ):
                position, orientation = self.inventory.getTraitValue( prop )
                self.register( prop, position, orientation )
                pass
            continue
        return


    def _init(self):
        Component._init(self)
        if self.inventory.dump: self._dump()
        return


    def _dump(self):
        lines = []
        lines.append('Report of geometrical info of components:')
        for prop in self.inventory.propertyNames():
            v = self.inventory.getTrait( prop )
            if isinstance( v, Register ):
                posr = self._positionRecord(prop)
                orir = self._orientationRecord(prop)
                pos = self.position(prop)
                ori = self.orientation(prop)
                lines.append('%s: %s, %s\n   abs. coords: %s, %s\n' % (
                        prop, posr, orir, pos, ori))
                continue
            continue
        
        print('\n'.join(lines))
        return

    pass # end of Geometer

import numpy as np


def test():
    class G(Geometer):
        class Inventory(Geometer.Inventory):
            a = Register('a')
            pass
        pass
    g = G()
    g._configure()
    g._init()
    print(g.position( 'a' ), g.orientation( 'a' ))
    return

if __name__ == '__main__': test()

# version
__id__ = "$Id$"

# End of file 
