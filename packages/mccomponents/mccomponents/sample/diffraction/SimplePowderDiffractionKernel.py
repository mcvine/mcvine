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


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SimplePowderDiffractionKernel(Kernel):

    '''a simple kernel for powder diffraction
    '''

    def __init__(self, Dd_over_d, DebyeWaller_factor, peaks):
        '''new SimplePowderDiffractionKernel
  Inputs:
    Dd_over_d: relative line width Delta_d/d
    DebyeWaller_factor: Debye-Waller factor
    peaks: data of all powder diffraction peaks. a peak should be an instance of Peak
    '''
        self.Dd_over_d = Dd_over_d
        self.DebyeWaller_factor = DebyeWaller_factor
        self.peaks = peaks
        return
        
    def identify(self, visitor): 
        return visitor.onSimplePowderDiffractionKernel(self)
    
    pass



class Data:

    peaks = [] # peaks should be a list of instances of Peak
    Dd_over_d = 0
    DebyeWaller_factor = 0
    density = 0
    atomic_weight = 0
    unitcell_volume = 0
    number_of_atoms = 0
    absorption_cross_section = 0
    incoherent_cross_section = 0


class Peak:

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


# version
__id__ = "$Id$"

# End of file 
