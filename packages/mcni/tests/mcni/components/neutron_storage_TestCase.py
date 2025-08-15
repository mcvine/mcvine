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

import os
os.environ['MCVINE_MPI_BINDING'] = 'NONE'


standalone = True


'''
Test of neutrons storage components

The behavior to test:

 - write neutrons to storage
 - read neutrons from storage
 - set packet size when write to storage
 - when writing neutrons to storage, the last packet (if it is not a complete
   packet) will be lost
'''



import unittestX as unittest



neutron_storage_path = 'neutrons'
ntotneutrons = 53
packetsize = 10
npackets = ntotneutrons//packetsize

import mcni
neutron = mcni.neutron( r = (0,0,0),
                        v = (1000,2000,3000),
                        time = 0,
                        prob = 1,
                        )


from mcni.AbstractComponent import AbstractComponent
class Source( AbstractComponent ):

    def process(self, neutrons):
        for i in range(len(neutrons)):
            neutrons[i] = mcni.neutron( r = (0,0,i), v = (1000, 2000, 3000) )
            continue
        return neutrons
    
    
class Verifier( AbstractComponent ):

    def __init__(self, name, testFacility):
        AbstractComponent.__init__(self, name)
        self.testFacility = testFacility
        return

    def process(self, neutrons):
        for n in neutrons: print(n)
        for i in range(len(neutrons)):
            r = list( neutrons[i].state.position )

            self.testFacility.assertVectorAlmostEqual(
                r, (0,0,i%ntotneutrons-1 ))
            
            v = list( neutrons[i].state.velocity )
            self.testFacility.assertVectorAlmostEqual(
                v, (2000,-1000,3000) )
            continue
        return neutrons

    pass # end of Verifier



class TestCase(unittest.TestCase):


    def test0(self):
        'prepare'
        import os
        if os.path.exists( neutron_storage_path ): 
            os.remove( neutron_storage_path )
        return


    def test1(self):
        'neutron --> storage'
        #from mcni.components.MonochromaticSource import MonochromaticSource
        #component1 = MonochromaticSource('source', neutron)
        component1 = Source( 'source' )
        
        from mcni.components.NeutronToStorage import NeutronToStorage
        component2 = NeutronToStorage( 'storage', neutron_storage_path)
        instrument = mcni.instrument( [component1, component2] )
        
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,1), (0,0,90) )

        neutrons = mcni.neutron_buffer( ntotneutrons )

        mcni.simulate( instrument, geometer, neutrons )
        return


    def test2(self):
        'storage --> verifier'
        from mcni.components.NeutronFromStorage import NeutronFromStorage
        component1 = NeutronFromStorage('storage', '%s-saved' % neutron_storage_path)
        component2 = Verifier( 'verifier', self)
        instrument = mcni.instrument( [component1, component2] )
        geometer = mcni.geometer()
        geometer.register( component1, (0,0,0), (0,0,0) )
        geometer.register( component2, (0,0,0), (0,0,0) )
        neutrons = mcni.neutron_buffer( packetsize*(npackets+1) )
        mcni.simulate( instrument, geometer, neutrons )
        return


    pass # end of TestCase


def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )

def main():
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
