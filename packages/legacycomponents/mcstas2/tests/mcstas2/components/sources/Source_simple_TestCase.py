#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


import numpy as np, unittest
from mcni.utils import conversion

componentname = 'Source_simple'
category = 'sources'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap Source_simple"
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        component = factory('component', E0=50., dE=0.001)
        E0 = component.E0
        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        component.process( neutrons )
        for n in neutrons:
            v = np.linalg.norm(n.state.velocity)
            E = conversion.v2e(v)
            self.assertAlmostEqual(E, E0, places=2)
        return

    def test2(self):
        "wrap Source_simple"
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        component = factory('component', E0=50., dE=0.001)
        E0 = component.E0 = 100.
        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        component.process( neutrons )
        for n in neutrons:
            v = np.linalg.norm(n.state.velocity)
            E = conversion.v2e(v)
            self.assertAlmostEqual(E, E0, places=2)
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
