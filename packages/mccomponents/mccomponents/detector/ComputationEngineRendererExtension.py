#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



class ComputationEngineRendererExtension:

    
    def onCompositeDetector(self, composite):
        factory = self.factory
        
        elements = composite.elements()
        geometer = composite.geometer
        
        cscatterers = factory.scatterercontainer()
        cgeometer = factory.geometer( )
        for index, element in enumerate(elements):
            
            #index is the index of this element in its container
            #this way array indexing will be easy.
            self._indexes_in_detsys.append( index )
            cscatterer = element.identify(self)
            self._indexes_in_detsys.pop()
            
            cscatterers.append( cscatterer )
            
            position = self._remove_length_unit( geometer.position(element) )
            cposition = factory.position( position )
            
            orientation = self._remove_angle_unit( geometer.orientation(element) )
            corientation = factory.orientation( orientation )
            
            cgeometer.register( cscatterer, cposition, corientation )
            continue
        
        cshape = composite.shape().identify(self)
        
        return factory.compositescatterer( cshape, cscatterers, cgeometer )


    def onDetectorPack(self, detectorPack):
        return self.onCompositeDetector( detectorPack )


    def onDetectorPackCopy(self, copy):
        pack = copy.reference()
        return self.onDetectorPack(pack)


    def onDetectorSystem(self, detectorSystem):
        #tof->channel converter
        tofmin, tofmax, tofstep = detectorSystem.tofparams
        t2c = self.factory.tof2channel(tofmin, tofmax, tofstep)
        
        #
        mca = detectorSystem.mca.identify(self)
        
        #attach to renderer so that detector elements can refer to them
        self.t2c_cinstance = t2c
        self.mca_cinstance = mca
        
        self._indexes_in_detsys = []
        ret = self.onCompositeDetector( detectorSystem )
        del self._indexes_in_detsys
        
        del self.mca_cinstance, self.t2c_cinstance
        return ret
    

    def onEventModeMCA(self, mca):
        return self.factory.eventmodemca( mca.outfilename, mca.detectorDims )


    def onHe3Tube( self, he3tube ):
        '''construct computation engine of given he3tube description'''
        from mccomposite.geometry import locate
        
        # assume all elements of he3tube are pixels
        pixels = he3tube.elements()
        npixels = len(pixels) 
        
        #shape of he3tube
        shape = he3tube.shape()
        if not shape: raise "shape of he3tube %s is not specified" % he3tube
        cshape = shape.identify(self)
        
        #make sure pixels are in the he3tube
        geometer = he3tube.geometer
        for element in pixels:
            position = geometer.position(element)/units.length.meter
            cposition = self.factory.position( position )
            assert self.factory.locate( cposition, cshape ) == "inside", \
                   "pixel at %s is not inside the tube %s" % (
                position, cshape)
            continue
        
        #find the axis direction of the he3tube tube
        pixel0position = geometer.position(pixels[0]) / units.length.meter
        axisDirection = geometer.position(pixels[-1]) / units.length.meter - pixel0position
        import numpy, numpy.linalg as nl
        axisDirection = numpy.array(axisDirection)
        len1 = float(nl.norm(axisDirection))
        axisDirection /= len1
        #detector length. len1 is the length of (n-1) pixels
        tubeLength = len1 * npixels / (npixels-1)
        
        #pressure
        pressure = he3tube.pressure()
        
        #kernel
        import mccomponents.detector as md
        kernel = md.he3tubeKernel(
            pressure, self._indexes_in_detsys,
            tubeLength, npixels, axisDirection, pixel0position)
        
        try:
            mcweights = he3tube.mcweights
        except AttributeError:
            mcweights = 0.9, 0, 0.1
            
        # treat this detector as  a homogeneous scatterer
        import mccomponents.homogeneous_scatterer as mh
        scatterer = mh.homogeneousScatterer(
            shape, kernel,
            mcweights = mcweights )
        ret = scatterer.identify(self)
        return ret

    
    def onHe3TubeCopy(self, copy):
        he3tube = copy.reference()
        return self.onHe3Tube(he3tube)
    
    
    def onHe3TubeKernel(self, he3tubekernel):
        t = he3tubekernel
        
        pressure = t.pressure
        #convert to SI
        import units
        pressure = pressure/units.pressure.pascal
        
        tubeIndexes = t.tubeIndexes
        
        return self.factory.he3tubekernel(
            pressure, tubeIndexes,
            t.tubeLength, t.npixels, t.axisDirection, t.pixel0position,
            self.t2c_cinstance, self.mca_cinstance )


    pass # end of ComputationEngineRendererExtension



def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError , "Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] )
        pass
    
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}



from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )


import units


# version
__id__ = "$Id$"

# End of file 
