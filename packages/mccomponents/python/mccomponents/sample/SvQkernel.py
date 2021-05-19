#!/usr/bin/env python
#
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SvQkernel(Kernel):

    def __init__(self,
                 absorption_coefficient = None,
                 scattering_coefficient = None,
                 SvQ = None
                 ):
        '''new S(vQ) kernel
  Inputs:
    absorption_coefficient, scattering_coefficient
    SvQ: S(Q vector) functor
    '''
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        self.SvQ = SvQ
        return

    def identify(self, visitor): return visitor.onSvQkernel(self)

    pass


# End of file 
