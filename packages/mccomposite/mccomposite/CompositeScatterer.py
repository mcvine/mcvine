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



class CompositeScatterer:
    

    def __init__(self, shape = None):
        from Geometer import Geometer
        self.geometer = Geometer()
        self._elements = []
        self._shape = shape
        return


    def addElement(self, element, position = (0,0,0), orientation = (0,0,0) ):
        self._elements.append(element)
        self.geometer.register(element, position, orientation)
        return


    def elements(self): return self._elements


    def identify(self, visitor): return visitor.onCompositeScatterer(self)


    def shape(self):
        if self._shape is None:
            from geometry.operations import union
            self._shape = union( [e.shape() for e in self.elements() ] )
            pass
        return self._shape
    

    pass # end of CompositeScatterer



# version
__id__ = "$Id$"


# End of file 
