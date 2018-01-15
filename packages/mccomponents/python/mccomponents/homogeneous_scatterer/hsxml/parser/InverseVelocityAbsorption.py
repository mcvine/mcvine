#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from AbstractNode import AbstractNode


class InverseVelocityAbsorption(AbstractNode):


    tag = "InverseVelocityAbsorption"
    
    def __init__(self, document, attributes):
        AbstractNode.__init__(self, document )
        # convert to dictionary
        attrs = {}
        for k,v in attributes.items(): attrs[str(k)] = self._parse(v)

        # new element
        self.element = self.elementFactory(**attrs)
        return


    def notify(self, parent):
        return self.element.identify( parent )


    def elementFactory(self, *args, **kwds):
        from mccomponents.homogeneous_scatterer.mu_calculators import InverseVelocityAbsorption
        return InverseVelocityAbsorption( *args, **kwds )
    
    
    def onElement(self, element):
        self.element.addElement( element )
        return

    onCompositeKernel = onElement

    pass # end of CompositeKernel
    


# version
__id__ = "$Id$"

# End of file 
