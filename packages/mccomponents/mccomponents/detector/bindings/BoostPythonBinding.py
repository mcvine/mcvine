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



from mccomponents.homogeneous_scatterer.bindings.BoostPythonBinding import BoostPythonBinding, extend

import mccomponents.mccomponentsbp as b
import mccomposite.mccompositebp as b1


class New:

    def eventmodemca( self, outfilename, detectorDims ):
        '''eventmodemca( outfilename, detectorDims ): new event-mode mca
        outfilename: output file name
        detectorDims: detector dimensions.
          For example, if a detectory system has 15 packs, 8 tubes per pack, 128 pixels per tube, then
            detectorDims = 15,8,128
            
        '''
        dims = b.vector_uint( 0 )
        for dim in detectorDims: dims.append(dim)
        return b.EventModeMCA( outfilename, dims )

    
    def tof2channel( self, tofmin, tofmax, tofstep ):
        return b.Tof2Channel( tofmin, tofmax, tofstep )
    
    
    def he3tubekernel(self, pressure, tubeIndexes,
                      tubeLength, npixels, axisDirection, pixel0position,
                      t2c, mca):
        '''create a he3tube kernel in boost python binding

        pressure: pressure of He3 in tube. unit: atm
        tubeIndexes: indexes of this tube in the detector system
        tubeLength: length of the tube. unit: meter
        npixels: number of pixels
        axisDirection: direction vector of the axis of the detector
        pixel0position: position vector of the pixel #0 relative to the center of the tube
          Positions of pixels can be calculated by
              pixel0position + i * (axisDirection * tubeLength) / npixels
        t2c: time->channel converter
        mca: multichannel analyzer
        '''
        
        #c representation of tube indexes
        ctubeIndexes = b.vector_int(0)
        for ind in tubeIndexes: ctubeIndexes.append( ind )
        
        axisDirection = b1.Vector(*axisDirection)
        pixel0position = b1.Vector(*pixel0position)
        # mapper to map "z" to pixel ID
        cz2c = b.Z2Channel(tubeLength, npixels, axisDirection, pixel0position)

        return b.He3TubeKernel( pressure, ctubeIndexes, cz2c, t2c, mca )

    pass # end of BoostPythonBinding


extend( New )


# version
__id__ = "$Id$"

# End of file 
