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


from AbstractNode import AbstractNode


class CompositeKernel(AbstractNode):


    tag = "compositekernel"
    
    def __init__(self, document, attributes):
        AbstractNode.__init__(self, document )
        
        # convert to dictionary
        attrs = {}
        for k,v in attributes.items(): attrs[str(k)] = v

        # new element
        self.element = self.elementFactory(**attrs)

        return


    def notify(self, parent):
        return self.element.identify( parent )


    def elementFactory(self, *args, **kwds):
        from mccomponents.homogeneous_scatterer import compositeKernel
        return compositeKernel( *args, **kwds )
    
    
    def onElement(self, element):
        self.element.addElement( element )
        return

    onCompositeKernel = onElement

    pass # end of CompositeKernel
    


# version
__id__ = "$Id$"

# End of file 
