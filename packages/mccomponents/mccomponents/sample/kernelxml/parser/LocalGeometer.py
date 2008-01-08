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


class LocalGeometer(Node):

    tag = "LocalGeometer"
     
    def __init__(self, document, attributes):
        Node.__init__(self, document)
        self._pinfos = []
        self._coord_system = attributes.get('registry-coordinate-system')
        if self._coord_system is None:
            self._coord_system = 'InstrumentScientist'
        return


    def notify(self, parent):
        #parent is a xml node. parent.element is a sampleassembly element
        #that the geometer should attach to
        target = parent.element

        #create geometer
        import sampleassembly.geometers as ig
        geometer = ig.local_geometer(
            target, registry_coordinate_system = self._coord_system )

        #register elements
        for pinfo in self._pinfos:
            name = pinfo.objname
            element = target.elementFromName( name )
            geometer.register(element , pinfo.position, pinfo.orientation)
            continue
        geometer.finishRegistration()

        #attach to target
        target.local_geometer = geometer

        #add geometer to the geometer list
        document = self.document
        try:
            geometers = document.geometers
        except AttributeError :
            geometers = document.geometers = []
            pass        
        geometers.append( geometer )
        
        return geometer


    def onRegister(self, register):
        #element must be "Register"
        pinfo = register.pinfo
        self._pinfos.append( pinfo )
        return

    pass # end of LocalGeometer
    


# version
__id__ = "$Id: Geometer.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
