
from mccomponents.homogeneous_scatterer.Kernel import Kernel
class He3TubeKernel(Kernel):

    def __init__(self, pressure, tubeIndexes, 
                 tubeLength, npixels, axisDirection, pixel0position):
        '''new He3 detector tube kernel
        pressure: gas pressure of He3. with units
        tubeIndexes: indexes to identify the tube
        '''
        self.pressure = pressure
        self.tubeIndexes = tubeIndexes
        self.tubeLength = tubeLength
        self.npixels = npixels
        self.axisDirection = axisDirection
        self.pixel0position = pixel0position
        return
        
    def identify(self, visitor): return visitor.onHe3TubeKernel(self)
    
    pass


#register new kernel type
# 2. the handler to construct c++ engine
def onHe3TubeKernel(self, he3tubekernel):
    
    t = he3tubekernel
    
    pressure = t.pressure
    #convert to SI
    import units
    pressure = pressure/units.pressure.pascal

    tubeIndexes = t.tubeIndexes
    
    return self.factory.he3tubekernel(
        pressure, tubeIndexes,
        t.tubeLength, t.npixels, t.axisDirection, t.pixel0position)


# 3. the handler to call python bindings
def he3tubekernel(self, pressure, tubeIndexes,
                  tubeLength, npixels, axisDirection, pixel0position):
    import mccomponents.mccomponentsbp as b
    import mccomposite.mccompositebp as b1

    #c representation of tube indexes
    ctubeIndexes = b.vector_int(0)
    for ind in tubeIndexes: ctubeIndexes.append( ind )

    axisDirection = b1.Vector(*axisDirection)
    pixel0position = b1.Vector(*pixel0position)
    cz2c = b.Z2Channel(tubeLength, npixels, axisDirection, pixel0position)

    return b.He3TubeKernel( pressure, ctubeIndexes, cz2c, self.t2c, self.mca )


import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register (
    He3TubeKernel, onHe3TubeKernel,
    {'BoostPythonBinding':he3tubekernel} )
