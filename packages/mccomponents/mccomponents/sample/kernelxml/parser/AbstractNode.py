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
debug = journal.debug("scatteringkernel.xmlparser")


from pyre.xml.Node import Node
import urllib



class XMLFormatError(Exception): pass


class AbstractNode(Node):

    def __init__(self, document, attributes):
        Node.__init__(self, document)

        # convert to dictionary
        attrs = {}
        for k,v in attributes.items(): attrs[str(k)] = v

        # new element
        self.element = self.elementFactory(**attrs)

        return


    def elementFactory(self, *args, **kwds):
        raise NotImplementedError


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


    def _parse(self, expr):
        return self._parser.parse(expr)

    from pyre.units import parser
    _parser = parser()
    pass




# version
__id__ = "$Id: AbstractNode.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
