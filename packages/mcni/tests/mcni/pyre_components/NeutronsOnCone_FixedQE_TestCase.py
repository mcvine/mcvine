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

debug = journal.debug( "mcni.pyre_components.test" )
warning = journal.warning( "mcni.pyre_components.test" )


Q = 8
E = 30
Ei = 70
L1 = 11


class TestCase(unittest.TestCase):

    def test(self):
        'mcni.pyre_components.NeutronsOnCone_FixedQE'
        from mcni.pyre_components.NeutronsOnCone_FixedQE import NeutronsOnCone_FixedQE as factory
        component = factory( 'source' )
        component.inventory.Q = Q
        component.inventory.E = E
        component.inventory.Ei = Ei
        component.inventory.L1 = L1
        component._configure()
        component._init()

        import mcni
        neutrons = mcni.neutron_buffer( 10 )
        component.process( neutrons )
        from numpy.linalg import norm
        from mcni.utils import v2e, e2v, v2k
        vi = e2v( Ei )
        t = L1/vi
        for n in neutrons:
            vv = n.state.velocity
            vQv = -vv[0], -vv[1], vi-vv[2]
            vQ = norm(vQv)
            Q1 = v2k(vQ)
            v = norm( vv )
            self.assertAlmostEqual( v2e(v), Ei-E, 4)
            self.assertAlmostEqual( n.time, t, 4 )
            self.assertAlmostEqual( Q, Q1, 4 )
            continue

        component._fini()
        return
        

    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
    #debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
