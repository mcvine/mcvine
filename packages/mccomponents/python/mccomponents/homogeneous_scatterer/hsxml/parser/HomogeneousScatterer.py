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


#from pyre.xml.Node import Node
from AbstractNode import AbstractNode as base


class HomogeneousScatterer(base):


    tag = "homogeneous_scatterer"
    
    
    def __init__(self, document, attributes):
        base.__init__(self, document)
        
        # mcweights
        mcweights = attributes.get( 'mcweights' )
        if mcweights:
            mcweights = self._parse( mcweights )
        else:
            mcweights = 0, 1, 0.05
        if mcweights[2] == 0.:
            import warnings
            warnings.warn("Transmission weight is zero. This may cause problems for hollow shapes in single-scattering-only simulations (the shadowed parts won't be simulated)")
        self._mcweights = mcweights
        
        # max_multiplescattering_loops
        mml = attributes.get('max_multiplescattering_loops')
        if mml: mml = int(mml)
        self._max_multiplescattering_loops = mml
        
        # min_neutron_probability
        mnp = attributes.get('min_neutron_probability')
        if mnp: mnp = float(mnp)
        self._min_neutron_probability = mnp
        
        # packing_factor
        pf = attributes.get('packing_factor')
        if pf: pf = float(pf)
        self._packing_factor = pf
        return


    def notify(self, parent):
        #shape might come from sample assembly xml
        try: shape = self._shape
        except: shape = None
        #
        kernel = self._kernel
        mcweights = self._mcweights
        max_multiplescattering_loops = self._max_multiplescattering_loops
        min_neutron_probability = self._min_neutron_probability
        packing_factor = self._packing_factor
        
        from mccomponents.homogeneous_scatterer import homogeneousScatterer
        scatterer = homogeneousScatterer(
            shape, kernel,
            mcweights = mcweights,
            max_multiplescattering_loops = max_multiplescattering_loops,
            min_neutron_probability = min_neutron_probability,
            packing_factor = packing_factor,
            )
        
        #parent is the Document node. 
        parent.document = scatterer
        return


    def onKernel(self, kernel):
        self._kernel = kernel
        return


    onCompositeKernel = onKernel


    def onShape(self, shape):
        self._shape = shape
        return

    onCylinder = onBlock = onSphere = onShape

    pass # end of HomogeneousScatterer
    


# version
__id__ = "$Id$"

# End of file 
