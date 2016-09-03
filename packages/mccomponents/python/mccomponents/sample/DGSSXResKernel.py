#!/usr/bin/env python
#
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class DGSSXResKernel(Kernel):

    '''a kernel for DGS Single Crystal Resolution Calculation
    '''

    def __init__(
        self,
        target_position, target_radius,
        tof_at_target, dtof,
        absorption_cross_section = None,
        scattering_cross_section = None,
    ):
        '''new DGSSXResKernel
  Inputs:
    target_position, target_radius: position and radius of the target
    tof_at_target: desired TOF at target
    dtof: tof width
    absorption_cross_section, scattering_cross_section: cross sections
    '''
        self.target_position = target_position
        self.target_radius = target_radius
        self.tof_at_target = tof_at_target
        self.dtof = dtof
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        return
        
    def identify(self, visitor): return visitor.onDGSSXResKernel(self)
    
    pass



# version
__id__ = "$Id$"

# End of file 
