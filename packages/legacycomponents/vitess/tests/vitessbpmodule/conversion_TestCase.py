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
import numpy as np

N = 10

class TestCase(unittest.TestCase):


    def test1(self):
        "mcvine -> vitess"
        from vitess import vitessbp 
        from mcni import neutron_buffer, neutron
        b = neutron_buffer(N)
        for i in range(N):
            b[i] = neutron(r=(i,i,i), v=(i,i,i), prob=i, time=i)
            continue
        vnb = vitessbp.neutronbuffer2vitess(b)
        print len(vnb.getCharPtr())
        print type(vnb.getCharPtr())
        # print vnb.getCharPtr()
        open('out-testwritebuffer', 'wb').write(vnb.getCharPtr())
        return

    
    def test2(self):
        "vitess -> mcvine"
        from vitess import vitessbp 
        s = open('out-testwritebuffer', 'rb').read()
        from mcni import neutron_buffer
        nb = neutron_buffer(N)
        vitessbp.vitessbuffer2mcvinebuffer(s, N, nb)
        for i in range(N):
            n = nb[i]
            self.assert_((np.array(n.state.position)==(i,i,i)).all())
            self.assert_((np.array(n.state.velocity)==(i,i,i)).all())
            self.assertAlmostEqual(n.time, i)
            self.assertAlmostEqual(n.probability, i)
            continue
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
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
