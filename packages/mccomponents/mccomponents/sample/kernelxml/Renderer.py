#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                      California Institute of Technology
#                      (C)    2007   All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.weaver.mills.XMLMill import XMLMill
from pyre.geometry.pml.Renderer import Renderer as ShapeRenderer


class Renderer(ShapeRenderer, XMLMill):


    def render(self, instrument):
        document = self.weave(instrument)
        return document


    # handlers

    def onSampleAssembly(self, sampleassembly):
        self.sampleassembly = sampleassembly
        
        self._rep += ['', '<!DOCTYPE sampleassembly>', '']

        self._preElement( sampleassembly )
        self._expandElementContainer( sampleassembly )
        #ig = sampleassembly.geometer
        #self.onGlobalGeometer( ig )
        self._postElement( sampleassembly )
        return

    
    def onElementContainer(self, elementContainer):
        self._preElement( elementContainer )
        self._expandElementContainer( elementContainer )
        self._postElement( elementContainer )
        return
    

    def onElement(self, element):
        self._preElement( element )
        shape = element.shape()
        if shape: self.onShape( shape )
        self._postElement(element)
        return

    
    def _expandElementContainer(self, elementContainer):
        shape = elementContainer.shape()
        if shape : self.onShape( shape )
        
        for element in elementContainer.elements():
            element.identify(self)
            continue
        
        lgeometer = elementContainer.local_geometer
        self.onLocalGeometer( lgeometer )
        return


    def _preElement(self, element):
        self._write('')
        t = element.__class__.__name__
        self._write(
            '<%s %s>' % (t, attribs_str( element.attributes ) ) )
        
        self._indent()
        return


    def _postElement(self, element):
        t = element.__class__.__name__
        
        self._outdent()
        
        self._write( '</%s>' % t )
        self._write('')
        return


    onPowderSample = onElement


    def onLocalGeometer(self, geometer ):
        cs = geometer.registry_coordinate_system()
        self._write('<LocalGeometer registry-coordinate-system="%s">'%
                    cs.name)
        
        target = geometer.target

        self._indent()
        for element in target:
            position = tuple(geometer.position( element ) )
            orientation = tuple( geometer.orientation( element ) )
            self._write(
                '<Register name="%s" position="%s" orientation="%s"/>' % (
                element.name, position, orientation )
                )
            continue
        self._outdent()

        self._write('</LocalGeometer>')
        return


    def onGlobalGeometer( self, geometer ):
        
        cs = geometer.registry_coordinate_system()

        t = geometer.__class__.__name__
        postfix = 'Geometer' 
        assert t.endswith( postfix )
        t = t[:-len( postfix )].lower()
        
        self._write(
            '<GlobalGeometer registry-coordinate-system="%s" '\
            'type="%s" />' % (
            cs.name, t)
            )
        return


    def onShape(self, shape):
        self._write('<Shape>')
        #self._synchronizeRenderers()
        #shape.identify(self._shapeRenderer)
        shape.identify(self)
        self._write('</Shape>')
        return
    

    def __init__(self):
        XMLMill.__init__(self)
        ShapeRenderer.__init__(self)
        #self._shapeRenderer = ShapeRenderer()
        return


    def _renderDocument(self, document):
        return document.identify(self)


##     def _synchronizeRenderers(self):
##         self._shapeRenderer._rep = self._rep
##         return
    

    pass # end of Renderer


def attribs_str( attributes ):
    return ' '.join(
        ['%s="%s"' % (k, attributes.get(k)) for k in attributes ] )
        


# version
__id__ = "$Id: Renderer.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
