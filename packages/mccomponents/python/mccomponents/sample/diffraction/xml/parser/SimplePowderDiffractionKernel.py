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


from .KernelNode import KernelNode as base


class SimplePowderDiffractionKernel(base):


    tag = "SimplePowderDiffractionKernel"
    

    def createKernel( self, **kwds ):
        Dd_over_d = self._parse( kwds['Dd_over_d'] )
        DebyeWaller_factor = self._parse( kwds['DebyeWaller_factor'] )
        
        peakspath = kwds.get('peaks-py-path')
        lazpath = kwds.get('laz-path')
        
        if peakspath:
            env = {}
            s = open(peakspath).read()
            exec(s, env)
            peaks = env['peaks']
            unitcell_volume = env['unitcell_volume']
            xs = env['cross_sections']
        elif lazpath:
            from mccomponents.sample.diffraction.parsers.laz import parse
            laz = parse(open(lazpath).read())
            peaks = laz.peaks
            unitcell_volume = laz.lattice.volume
            xs = laz.cross_sections
        else:
            raise ValueError("SimplePowderDiffractionKernel needs path to "\
                  "the peaks datafile (laz or peaks.py)")
        
        from mccomponents.sample.diffraction import simplepowderdiffractionkernel as f
        return f(Dd_over_d, DebyeWaller_factor, peaks, 
                 unitcell_volume=unitcell_volume, cross_sections=xs)


    pass # end of SimplePowderDiffractionKernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onSimplePowderDiffractionKernel = HomogeneousScatterer.onKernel


# version
__id__ = "$Id$"

# End of file 
