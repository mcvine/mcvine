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


class SampleAssembly(AbstractNode):


    tag = "SampleAssembly"
    
    from sampleassembly.elements.SampleAssembly import SampleAssembly as ElementFactory

    onPowderSample = AbstractNode.onElement

    def notify(self, parent):
        document = self.document
        assert parent is document
        sampleassembly = document.sampleassembly
        assert self.element is sampleassembly

        return self.element.identify( parent )
        

    pass # end of SampleAssembly
    


# version
__id__ = "$Id: SampleAssembly.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
