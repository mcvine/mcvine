#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def loadPattern(xyz, laz):
    text = open(laz).read()
    from mccomponents.sample.diffraction.parsers.laz import parse
    peaks = parse(text).peaks
        
    # load structure
    from sampleassembly.crystal.ioutils import xyzfile2unitcell
    structure = xyzfile2unitcell(xyz)
    
    # diffraction pattern
    return DiffractionPattern(structure, peaks)



def total_scattering_cross_section(Ei, dp):
    """compute the total scattering cross section
    by powder diffraction
    from the given known list of peaks.
    This cross section is per unit cell.
    
    According to Squires, cross section by one Debye Scherrer cone is
    \sigma_{\tau} = 1/v_0 \lambda^3/(4sin(\theta/2)) \sum_{all \tau\prime of same length} |F_N(\tau\prime)|^2

    The total cross section is the sum of all such cones
    (number of cones is limited by Ei)
    
    Limitation: 
     * the diffraction peaks list usually could be limited
       if they are loaded from a file such as laz.
       Probably better be computed directly from the structure.
       When the peaks list is limited, the calculation
       would be wrong when Ei gets larger 
       (should see more diff peaks but they are not counted).
     * only  consider the ideal powder diffraction without
       vibrations. 
    """
    from mcni.utils import conversion as conv
    import numpy as np
    k = conv.e2k(Ei)
    l = np.pi * 2 / k
    ucvol = dp.structure.lattice.getVolume()
    # loop over peaks, for each peak that contributes
    # add its contribution
    sigma = 0
    for peak in dp.peaks:
        q = peak.q
        if q > 2*k: continue
        sinthetaover2 = q/2/k
        F_squared = peak.F_squared
        mul = peak.multiplicity
        sigma += l**3 / ucvol / 4 / sinthetaover2 * F_squared * mul
        continue
    return sigma


class Peak:

    "a powder diffraction peak"

    q = 0
    F_squared = 0
    multiplicity = 0
    intrinsic_line_width = 0
    DebyeWaller_factor = 0
    
    def __init__(self, **kwds):
        for k, v in kwds.iteritems():
            setattr(self, k, v)
            continue
        return


    def __repr__(self):
        return "Peak(q=%s, F_squared=%s, multiplicity=%s, intrinsic_line_width=%s, DebyeWaller_factor=%s" % (
            self.q, self.F_squared, self.multiplicity, self.intrinsic_line_width, self.DebyeWaller_factor)


class DiffractionPattern:

    def __init__(self, structure, peaks):
        self.structure = structure
        self.peaks = peaks
        return
    

# version
__id__ = "$Id$"

# End of file 
