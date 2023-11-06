#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class LorentzianBroadened_E_Q_Kernel(Kernel):

    '''S(Q,E) = S(Q) * lorentzian_distribution(gamma(Q))(E-E(Q))
    '''

    def __init__(
            self,
            E_Q = None,
            S_Q = None,
            gamma_Q = None,
            Qmin = None, Qmax = None,
            absorption_coefficient = None,
            scattering_coefficient = None,
    ):
        '''new E_Q kernel
  Inputs:
    E_Q: E(Q) function. str
    S_Q: S(Q) function. str
    gamma_Q: gamma(Q) function. str
    Qmin, Qmax: Q range. angstrom**-1
    absorption_coefficient, scattering_coefficient: m*-1
    '''
        self.E_Q = E_Q
        self.S_Q = S_Q
        self.gamma_Q = gamma_Q
        self.Qmin = Qmin
        self.Qmax = Qmax
        self.absorption_coefficient = absorption_coefficient
        self.scattering_coefficient = scattering_coefficient
        return

    def identify(self, visitor): return visitor.onLorentzianBroadened_E_Q_Kernel(self)

    pass


# End of file
