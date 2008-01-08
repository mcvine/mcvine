#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
debug = journal.debug("sampleassembly.xmlparser")


from pyre.xml.Node import Node
import urllib



class XMLFormatError(Exception): pass


class AbstractNode(Node):

    ElementFactory = None # overload this to provide factory method of creating element

    def __init__(self, document, attributes):
        Node.__init__(self, document)

        try:
            name = attributes['name']
        except KeyError:
            print attributes.keys()
            raise XMLFormatError, \
                  "Element does not have the 'name' attribute."\
                  "Element type: %s" % (
                self.__class__.__name__ )

        # convert to dictionary
        attrs = {}
        for k,v in attributes.items(): attrs[str(k)] = v
        del attrs['name']

        # see if we have sampleassembly instance established
        try:
            sampleassembly = document.sampleassembly
        except AttributeError :
            sampleassembly = None
            
        # new element
        self.element = self.ElementFactory(name, **attrs)

        #register guid, element pair
        if sampleassembly is None and isSampleAssembly(self.element):
            #establish sampleassembly instance
            document.sampleassembly = sampleassembly = self.element
            pass
        if sampleassembly is None:
            raise RuntimeError, "Sampleassembly is not yet defined"
        #sampleassembly.guidRegistry.register( self.element.guid(), self.element )
        
        return


    def notify(self, parent):
        return self.element.identify( parent )


    def content(self, content):
        debug.log( "content=%s" % content )
        content = content.strip()
        if len(content)==0: return
        self.element.appendContent( urllib.unquote(content).strip() )
        self.locator = self.document.locator
        return


    def onElement(self, element):
        self.element.addElement( element )
        return

    pass



def isSampleAssembly( element ):
    from sampleassembly.elements.SampleAssembly import SampleAssembly
    return isinstance( element, SampleAssembly )


# version
__id__ = "$Id: AbstractNode.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
