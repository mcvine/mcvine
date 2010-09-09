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


I = ( (1.,0,0),
      (0,1.,0),
      (0,0,1.), )
    

class Coord(object): 

    def __init__(self, value):
        self.value = value


class RelativeCoord(Coord):
    
    def __init__(self, value, to=None):
        if to is None:
            raise ValueError, "relative coord must specify the reference"
        super(RelativeCoord, self).__init__(value)
        self.reference = to
        self.isabsolute = False
        self.isrelative = True
        return


    def __str__(self):
        return '%s relative to %s' % (self.value, self.reference)


    def __repr__(self):
        v = self.value
        if not isinstance(v, basestring):
            v = str(tuple(v))
        ref = self.reference
        return "relative(%s, to='%s')" % (v, ref)


class AbsoluteCoord(Coord):
    
    def __init__(self, value):
        super(AbsoluteCoord, self).__init__(value)
        self.isabsolute = True
        self.isrelative = False
        return


    def __str__(self):
        return '%s' % (self.value, )


    def __repr__(self):
        v = self.value
        if isinstance(v, basestring): return v
        return str(tuple(self.value))


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
        if isinstance(value, basestring):
            env = {'relative': RelativeCoord}
            value = eval(value, env)
            pass
        
        try:
            n = len(value)
        except:
            raise ValueError, "%s. Should be a 2-tuple. Good examples: %s" % (
                value, good_records)

        if n != 2:
            raise ValueError, "%s. Should be a 2-tuple. Good examples: %s" % (
                value, good_records)

        pos, ori = value
        pos = _toCoord(pos)
        ori = _toCoord(ori)
        
        return pos, ori


good_records = """
  * (0,0,3), (0,0,0)
  * (0,0,3), relative((0,0,90), to='previous')
  * relative((0,0,3), to='sample'), (0,0,0)
"""

default_record = AbsoluteCoord((0,0,0)), AbsoluteCoord((0,0,0))



def _toCoord(candidate):
    if isinstance(candidate, Coord): return candidate
    assert len(candidate) == 3, "coord must be a 3-vector"
    return AbsoluteCoord(candidate)
    

from mcni.Geometer import Geometer as base

class Geometer(Component, base):

    
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


    def position(self, element):
        if element in self._abspos:
            return self._abspos[element]
        ret = self._abspos[element] = self._calcAbsPosition(element)
        return ret


    def orientation(self, element):
        if element in self._absori:
            return self._absori[element]
        ret = self._calcAbsOrientation(element)
        ret = np.array(ret)
        self._absori[element] = ret
        return ret
    
    
    def _calcAbsPosition(self, element):
        rec = self._positionRecord(element)
        rec = _toCoord(rec)
        if rec.isabsolute: return rec.value
        ref = rec.reference
        refpos = self.position(ref)
        refori = self.orientation(ref)
        return self.transformer(refpos, refori, rec.value, I)[0]


    def _calcAbsOrientation(self, element):
        rec = self._orientationRecord(element)
        rec = _toCoord(rec)
        if rec.isabsolute: return rec.value
        ref = rec.reference
        refpos = (0,0,0)
        refori = self.orientation(ref)
        ret = self.transformer(refpos, refori, (0,0,0), rec.value)[1]
        return ret


    def _positionRecord(self, element):
        try:
            return base.position( self, element )
        except:
            try:
                return base.position( self, element.name )
            except:
                #end to try out all aliases
                for alias in element.aliases:
                    try: return base.position( self, alias )
                    except: pass
                    continue
                #still nothing
                raise "Position of element %s not registered" % element.name


    def _orientationRecord(self, element):
        try:
            return base.orientation( self, element )
        except:
            try:
                return base.orientation( self, element.name )
            except:
                #end to try out all aliases
                for alias in element.aliases:
                    try: return base.orientation( self, alias )
                    except: pass
                    continue
                #still nothing
                raise "Orientation of element %s not registered" % element.name


    def _configure(self):
        Component._configure(self)
        for prop in self.inventory.propertyNames():
            v = self.inventory.getTrait( prop )
            if isinstance( v, Register ):
                position, orientation = self.inventory.getTraitValue( prop )
                self.register( prop, position, orientation )
                pass
            continue

        self.transformer = self.inventory.transformer

        self._abspos = {}
        self._absori = {}
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
        
        print '\n'.join(lines)
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
    print g.position( 'a' ), g.orientation( 'a' )
    return

if __name__ == '__main__': test()

# version
__id__ = "$Id: Channel.py,v 1.1.1.1 2005/03/08 16:13:53 aivazis Exp $"

# End of file 
