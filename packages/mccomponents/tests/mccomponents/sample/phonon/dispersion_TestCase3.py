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



import pylab
import unittestX as unittest
import journal

#debug = journal.debug( "TestCase" )
#warning = journal.warning( "TestCase" )


import mcni
import numpy


datapath = 'data/bccMo296_bvk'


class TestCase(unittest.TestCase):


    def test2(self):
        from mccomponents.sample.phonon import periodicdispersion_fromidf
        dispersion = periodicdispersion_fromidf( datapath )
        
        from mccomponents.sample import scattererEngine
        disp = scattererEngine( dispersion )
        
        from mccomponents.sample.phonon.bindings import default
        binding = default()

        b = 2.001014429
        
        N = 20
        Qs = [
            [b/2,b/2,0],
            [0,0,0],
            [b,0,0],
            [b/2,b/2,b/2],
            [0,0,0],
            ]

        xs=[[] for i in range(3)]; ys=[[] for i in range(3)]
        segment = 0
        for start, end in zip(Qs[:-1], Qs[1:]):
            start = numpy.array(start)
            end = numpy.array(end)
            diff = end-start
            step = diff/N
            
            qs = [ start + step*i for i in range(N+1) ]
            
            for br in range(3):
                es = [ disp.energy(br, binding.Q(q)) for q in qs ]

                xs[br] += list(numpy.arange(0, 1.+1e-10, 1./N)+segment)
                ys[br] += es

            segment += 1

        for br in range(3):
            x = xs[br]
            y = ys[br]
            pylab.plot(x,y)
            
        pylab.show()
                                            
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
    unittest.TextTestRunner(verbosity=2).run(alltests)
    
    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
