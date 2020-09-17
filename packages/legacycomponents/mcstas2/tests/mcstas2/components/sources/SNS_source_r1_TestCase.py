#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest
import journal


componentname = 'SNS_source_r1'
category = 'sources'

class TestCase(unittest.TestCase):

    def test(self):
        "wrap SNS_source_r1"
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        component = factory(
            'component',
            S_filename="source_sct521_bu_17_1.dat",
            width=0.1, height=0.12,
            dist=2.5,
            xw=0.1, yh=0.12,
            Emin=50, Emax=70,
            )

        import mcni
        neutrons = mcni.neutron_buffer( 5 )
        for i in range(5):
            neutrons[i] = mcni.neutron(r=(0,0,-1), v=(0,0,3000), time = 0, prob = 1)
            continue
        component.process( neutrons )
        print(neutrons)
        return

    def test2(self):
        "SNS_source_r1: angling"
        from mcstas2 import componentfactory
        factory = componentfactory( category, componentname )
        Emin=59.99; Emax=60.01
        component = factory(
            'component',
            S_filename="source_sct521_bu_17_1.dat",
            width=0.001, height=0.001,
            dist=2.5,
            xw=0.001, yh=0.001,
            Emin=Emin, Emax=Emax,
            angling = 30,
            )

        import mcni
        N = 100
        neutrons = mcni.neutron_buffer( N )
        for i in range(N):
            neutrons[i] = mcni.neutron(r=(0,0,-1), v=(0,0,3000), time = 0, prob = 1)
            continue
        component.process( neutrons )

        from mcni.utils import conversion as Conv
        expected_vlen = Conv.e2v((Emin+Emax)/2)
        
        import numpy as np
        for i in range(N):
            neutron = neutrons[i]
            state = neutron.state
            r = state.position
            assert abs(r[0]) < 0.001
            assert abs(r[1]) < 0.001
            assert abs(r[2]) < 0.001
            v = np.array(state.velocity)
            vlen = np.linalg.norm(v)
            # print v, expected_vlen, vlen
            assert abs(vlen - expected_vlen)/expected_vlen < 0.01
            assert abs(-v[0] - expected_vlen/2.)/expected_vlen < 0.01
            assert abs(v[2] - expected_vlen*np.sqrt(3)/2.)/expected_vlen < 0.01
        return

    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug("CompositeNeutronScatterer_Impl").activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
