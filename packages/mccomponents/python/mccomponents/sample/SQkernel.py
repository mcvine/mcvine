#!/usr/bin/env python
#
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SQkernel(Kernel):

    def __init__(self,
                 absorption_coefficient = None,
                 scattering_coefficient = None,
                 SQ = None, Qrange = None,
                 ):
        '''new S(Q) kernel
  Inputs:
    absorption_coefficient, scattering_coefficient
    SQ: S(Q) functor
    Qrange: Q range (min, max)
    '''
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        self.SQ = SQ
        self.Qrange = Qrange
        return

    def identify(self, visitor): return visitor.onSQkernel(self)

    pass


# End of file
