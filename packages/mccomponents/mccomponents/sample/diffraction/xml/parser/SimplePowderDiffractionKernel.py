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


from AbstractNode import AbstractNode, debug


class SimplePowderDiffractionKernel(AbstractNode):


    tag = "SimplePowderDiffractionKernel"
    

    def elementFactory( self, **kwds ):
        Dd_over_d = self._parse( kwds['Dd_over_d'] )
        DebyeWaller_factor = self._parse( kwds['DebyeWaller_factor'] )

        peakspath = kwds.get('peaks-py-path')
        lazpath = kwds.get('laz-path')

        if peakspath:
            env = {}
            s = open(peakspath).read()
            exec s in env
            peaks = env['peaks']
        elif lazpath:
            from mccomponents.sample.diffraction.parsers.laz import parse
            peaks = parse(open(lazpath).read())
        else:
            raise ValueError, "SimplePowderDiffractionKernel needs path to "\
                  "the peaks datafile (laz or peaks.py)"
        
        from mccomponents.sample.diffraction import simplepowderdiffractionkernel as f
        return f(Dd_over_d, DebyeWaller_factor, peaks)


    pass # end of SimplePowderDiffractionKernel


from HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onSimplePowderDiffractionKernel = HomogeneousScatterer.onKernel


# version
__id__ = "$Id$"

# End of file 
