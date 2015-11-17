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


## This package provide supports for the "instrument" package at
## svn://danse.us/instrument


def getDetectorHierarchyDimensions( instrument ):
    return GetDetectorHierarchyDimensions().render( instrument )


def assignLocalGeometers( instrument, **kwds ):
    AssignLocalGeometers().render(instrument, **kwds)
    return


from instrument.elements.Visitor import Visitor

class GetDetectorHierarchyDimensions(Visitor):

    '''go thru a instrument representation (svn://danse.us/instrument)
    and obtain dimensions of detector hierarchy.
    For example, if a detector system has 30 packs, 8 He3 tube per pack,
    100 pixel per tube, then
      dims = [ ("DetectorPack", 30), ("He3Tube", 8), ("Pixel", 100) ]
    '''

    def render(self, instrument):
        geometer = instrument.geometer
        self._layers = []
        self._indexShape = []
        self._level = 0
        Visitor.render( self, instrument, geometer )
        ret = zip(self._layers, self._indexShape)
        del self._level, self._indexShape, self._layers
        return ret

    def onInstrument(self, instrument):
        for e in instrument: e.identify(self)
        return

    def onContainer(self, container):
        n = len( container.elements() ) 
        if self._level == len(self._indexShape):
            self._indexShape.append( n )
            # we are assuming all elements are the same type
            # should we check that?
            if n>0:
                typeName = container.elements()[0].__class__.__name__
                for e in container.elements()[1:]:
                    t = e.__class__.__name__
                    if t == 'Copy': t = e.reference().__class__.__name__
                    assert t == typeName, \
                           "typename mismatch: %s, %s" % (
                        typeName, t )
                self._layers.append( typeName )
                pass
                
        elif self._level < len(self._indexShape):
            self._indexShape[self._level] = max(self._indexShape[self._level], n )
            # we assume that this detector system is flattenable
            typeName = self._layers[self._level] 
            for e in container.elements():
                t = e.__class__.__name__
                if t == 'Copy': t = e.reference().__class__.__name__
                assert typeName == t, \
                       "typename mismatch: %s, %s" % (
                    typeName, e.__class__.__name__ )
                continue
        else:
            raise RuntimeError , "shape: %s, level: %s" %(
                self._indexShape, self._level)
        self._level += 1
        for element in container: element.identify( self )
        self._level -= 1
        return

    onDetectorSystem = onDetectorArray = onDetectorPack = onDetector = onContainer

    def doNothing(self, e): return
    onSample = onModerator = onMonitor = onGuide = onPixel = onCopy = doNothing

    pass # end of GetDetectorHierarchyDimensions
    

class AssignLocalGeometers:

    '''The instrument representation from the "instrument" package (svn://danse.us/instrument)
    has a "global geometer" attached to the instrument. But the nodes in the instrument
    does not have "local geometers" attach to them. In mccomponents, we
    require that any composite should have a local geoemter attached. 
    This class go thru the representation and assign local geometers to composite nodes.
    '''

    def render(self, instrument, coordinate_system = 'McStas'):
        from instrument.geometers import coordinateSystem
        self._cs = coordinateSystem( coordinate_system )
        
        self.global_geometer = instrument.global_geometer = instrument.geometer
        instrument.identify(self)
        del self.global_geometer
        return


    def onComposite(self, composite):
        geometer = self.global_geometer._getLocalGeometer( composite )
        geometer.changeRequestCoordinateSystem( self._cs )
        composite.geometer = geometer
        for element in composite.elements():
            element.identify(self)
        return


    def donothing(self, visitee): return


    onInstrument = onDetectorSystem = onDetectorPack = onDetector = onDetectorArray\
                   = onComposite


    onModerator = onMonitor = onSample = onGuide = onPixel = onCopy = donothing


    pass 


# version
__id__ = "$Id$"

# End of file 

