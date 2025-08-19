#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from .KernelNode import KernelNode as base


class SingleCrystalDiffractionKernel(base):


    tag = "SingleCrystalDiffractionKernel"

    def createKernel( self, **kwds ):
        Dd_over_d = self._parse( kwds['Dd_over_d'] )
        laupath = kwds.get('lau-path')
        if laupath:
            with open(laupath, 'rt') as stream:
                text = stream.read()
                from ...parsers import lau
                lau = lau.parse(text)
        else:
            raise ValueError("SingleCrystalDiffractionKernel needs path to "\
                  "the hkl datafile (lau)")
        hkllist = lau.hkls
        mosaic = self._parse(kwds.get('mosaic'))
        from mccomponents.sample.diffraction import singlecrystaldiffractionkernel as f
        basis_vectors = lau.lattice.base
        abs_xs = None
        return f(basis_vectors, hkllist, mosaic, Dd_over_d, abs_xs)

    pass # end of SingleCrystalDiffractionKernel


from .HomogeneousScatterer import HomogeneousScatterer
HomogeneousScatterer.onSingleCrystalDiffractionKernel = HomogeneousScatterer.onKernel


# End of file
