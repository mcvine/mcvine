#!/usr/bin/env python
#
#


from .KernelNode import KernelNode as base, debug

class SANSSpheresKernel(base):

    tag = "SANSSpheresKernel"

    def createKernel( self, **kwds ):
        def getval(key):
            v = kwds.get(key)
            if v: return self._parse(v)
            return v
        kargs = dict(
            abs_coeff = getval('abs_coeff'),
            R = getval('R'),
            phi = getval('phi'),
            delta_rho = getval('delta_rho'),
            max_angle = getval('max_angle'),
        )
        from mccomponents.sample.sans import spheres_kernel as f
        return f(**kargs)

    pass # end of SANSSpheresKernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onSANSSpheresKernel = HomogeneousScatterer.onKernel

# End of file
