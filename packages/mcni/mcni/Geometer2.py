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


'''a more intelligent geometer that allows users to specify
coordinates relative to peers
'''


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


from coordinate_system_transformers.mcstas import transformCoordinateSystem as defaultCoordTransformer


def _toCoord(candidate):
    if isinstance(candidate, Coord): return candidate
    assert len(candidate) == 3, "coord must be a 3-vector"
    return AbsoluteCoord(candidate)
    

import numpy as np



from Geometer import Geometer as base
class Geometer(base):

    #
    element_sequence = None # need this to support "previous"
    

    def __init__(self, transformer=None):
        super(Geometer, self).__init__()

        self._abspos = {}
        self._absori = {}
        
        if transformer is None:
            transformer = defaultCoordTransformer
        self.transformer = transformer
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
        ref = self._findReference(ref, element)
        refpos = self.position(ref)
        refori = self.orientation(ref)
        return self.transformer(refpos, refori, rec.value, I)[0]


    def _calcAbsOrientation(self, element):
        rec = self._orientationRecord(element)
        rec = _toCoord(rec)
        if rec.isabsolute: return rec.value
        ref = rec.reference
        ref = self._findReference(ref, element)
        refpos = (0,0,0)
        refori = self.orientation(ref)
        ret = self.transformer(refpos, refori, (0,0,0), rec.value)[1]
        return ret


    def _positionRecord(self, element):
        return base.position( self, element )


    def _orientationRecord(self, element):
        return base.orientation( self, element )


    def _findReference(self, ref, element):
        if ref == 'previous':
            seq = self.element_sequence
            if seq is None:
                raise RuntimeError, "sequence of elements were not set. Won't be able to deduce position/orientation using keyword 'previous'"
            i = seq.index(element)
            if i == 0:
                raise RuntimeError, "there is no previous element for %s" % element
            return seq[i-1]
        return ref
    

    pass # Geometer


# version
__id__ = "$Id$"

# End of file 
