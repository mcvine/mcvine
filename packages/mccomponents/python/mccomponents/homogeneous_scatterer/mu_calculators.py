#
# Jiao Lin <jiao.lin@gmail.com>
#

class InverseVelocityAbsorption:

    def __init__(self, mu_at_2200):
        self.mu_at_2200 = mu_at_2200
        return

    def identify(self, visitor):
        return visitor.onInverseVelocityAbsorption(self)


