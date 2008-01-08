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


from pyre.xml.Node import Node


class Shape(Node):


    tag = "Shape"
    
     
    def __init__(self, document, attributes):
        Node.__init__(self, document)
        return


    def notify(self, parent):
        #parent is a xml node. parent.element is a sampleassembly element
        #that this shape should be attached to
        target = parent.element
        target.setShape( self._shape )
        return 


    def on_(self, sth):
        self._shape = sth
        return

    onUnion = on_
    onCylinder = onBlock = on_

    pass # end of Shape
    


# version
__id__ = "$Id: Geometer.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
