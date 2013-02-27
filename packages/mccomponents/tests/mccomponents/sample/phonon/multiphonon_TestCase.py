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

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


import numpy


class TestCase(unittest.TestCase):


    def test1(self):
        from dos import loadDOS
        dos = loadDOS()
        dE = dos.energy[1] - dos.energy[0]
        from mccomponents.sample.phonon.multiphonon import computeAnESet
        kelvin2mev = 0.0862
        beta = 1./(300*kelvin2mev)
        E, An_set = computeAnESet(N=5, E=dos.energy, g=dos.I, beta=beta, dE=dE)
        import pylab
        for An in An_set:
            print An
            pylab.plot(E, An)
            continue
        pylab.show()
        return
        
        
    def test2(self):
        from dos import loadDOS
        dos = loadDOS()
        E = dos.energy; g = dos.I
        dE = E[1] - E[0]
        print len(E)
        
        Q = numpy.arange(0, 10, 0.1)
        dQ = Q[1] - Q[0]
        
        kelvin2mev = 0.0862
        beta = 1./(300*kelvin2mev)

        M = 50.
        
        from mccomponents.sample.phonon.multiphonon import computeSQESet
        Q, E, S_set= computeSQESet(5, Q, dQ, E, dE, M, g, beta)

        import histogram as H, histogram.hdf as hh
        import pylab
        for i, Sn in enumerate(S_set):
            # pylab.imshow(Sn.T)
            # pylab.show()
            h = H.histogram(
                'S%s' % (i+1),
                [('Q', Q, 'angstrom**-1'),
                 ('E', E, 'meV')],
                Sn)
            hh.dump(h, 'S%s.h5' % (i+1))
            continue
        return
        
        
    pass  # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main():
    #debug.activate()
    #journal.debug('phonon_coherent_inelastic_polyxtal_kernel').activate()
    #journal.debug('random').activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    res = unittest.TextTestRunner(verbosity=2).run(alltests)
    import sys; sys.exit(not res.wasSuccessful())

    
    
if __name__ == "__main__":
    unittest.main()
    #  main()
    
# version
__id__ = "$Id: dispersion_TestCase.py 1126 2011-04-10 03:05:40Z linjiao $"

# End of file 
