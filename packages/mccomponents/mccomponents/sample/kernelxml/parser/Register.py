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


from pyre.geometry.pml.parser.AbstractNode import AbstractNode


class Register(AbstractNode):

    tag = "Register"

    def __init__(self, document, attributes):
        AbstractNode.__init__(self, document)
        name = attributes.get('name')
        position = self._parse(attributes["position"])
        orientation = self._parse(attributes["orientation"])

        from sampleassembly.geometers.PositionalInfo import PositionalInfo
        self.pinfo = PositionalInfo( name, position, orientation )
        return


    def notify(self, parent):
        return parent.onRegister( self )

    pass # end of Register
    

# version
__id__ = "$Id$"

# End of file 
