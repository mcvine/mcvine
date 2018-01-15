#
# Jiao Lin <jiao.lin@gmail.com>
#

class InverseVelocityAbsorption:

    def __init__(self, mu_at_2200):
        self.mu_at_2200 = mu_at_2200
        return

    def identify(self, visitor):
        return visitor.onInverseVelocityAbsorption(self)



class InterpolateAbsorptionFromCurve:

    def __init__(self, energies, mus):
        self.energies = energies
        self.mus = mus
        return

    def identify(self, visitor):
        return visitor.onInterpolateAbsorptionFromCurve(self)
