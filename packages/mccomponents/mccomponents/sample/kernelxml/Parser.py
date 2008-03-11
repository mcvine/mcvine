#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.xml.Parser import Parser as ParserBase


class Parser(ParserBase):


    def parse(self, stream, parserFactory=None):

        from parser import getDocument
        Document = getDocument()
        
        document = Document(stream.name)
        return ParserBase.parse(
            self, stream, document, parserFactory)
    
    
    def __init__(self):
        ParserBase.__init__(self)
        return
           

# version
__id__ = "$Id: Parser.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
