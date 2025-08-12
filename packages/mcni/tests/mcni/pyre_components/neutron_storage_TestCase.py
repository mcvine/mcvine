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
os.environ['MCVINE_MPI_LAUNCHER'] = 'serial'


standalone = True


import unittestX as unittest


#input parameter for output directory for neutrontostorage component
instrument1_output = 'out-neutron_storage_TestCase'
instrument2_output = 'out-neutron_storage_TestCase-Instrument2'

#the real output directory depends on
# mpi is installed or not
instrument1_outputpath = instrument1_output
instrument2_outputpath = instrument2_output


import shutil
if os.path.exists( instrument1_outputpath ):
    shutil.rmtree( instrument1_outputpath )
if os.path.exists( instrument2_outputpath ):
    shutil.rmtree( instrument2_outputpath )

neutron_storage_path = 'neutrons'


from mcni.pyre_support.Instrument import Instrument as base
class Instrument1(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility

        from mcni.pyre_components.MonochromaticSource import MonochromaticSource 
        source = facility('source', default = MonochromaticSource('source') )

        from mcni.pyre_components.NeutronToStorage import NeutronToStorage
        storage = facility('storage', default = NeutronToStorage( 'storage' ) )

        pass # end of Inventory


    def _defaults(self):
        base._defaults(self)
        # serial mode
        self.inventory.mode = 'worker'
        from mcni.pyre_support.LauncherSerial import LauncherSerial
        self.inventory.launcher = LauncherSerial()

        self.inventory.sequence = ['source', 'storage']
        
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.source = (0,0,0), (0,0,0)
        self.inventory.geometer.inventory.storage = (0,0,1), (0,0,0)

        source = self.inventory.source
        source.inventory.position = '0,0,0'
        source.inventory.velocity = '1000,2000,3000'

        storage = self.inventory.storage
        storage.inventory.path = neutron_storage_path
        return
    
    pass # end of Instrument1



from mcni.pyre_support.AbstractComponent import AbstractComponent
class Verifier( AbstractComponent ):

    def setTestFacility(self, testFacility):
        self.testFacility = testFacility
        return

    def process(self, neutrons):
        for i in range(len(neutrons)):
            r = list( neutrons[i].state.position )
            self.testFacility.assertVectorAlmostEqual(
                r, (0,0,-1) )
            
            v = list( neutrons[i].state.velocity )
            self.testFacility.assertVectorAlmostEqual(
                v, (1000,2000,3000) )
            continue
        return neutrons

    pass # end of Verifier



class Instrument2(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility

        from mcni.pyre_components.NeutronFromStorage import NeutronFromStorage
        source = facility('source', default = NeutronFromStorage('source') )

        verifier = facility('verifier', default = Verifier( 'verifier' ) )

        pass # end of Inventory


    def main(self):
        self.inventory.verifier.setTestFacility( self.testFacility )
        base.main(self)
        return


    def _defaults(self):
        base._defaults(self)
        # serial mode
        self.inventory.mode = 'worker'
        from mcni.pyre_support.LauncherSerial import LauncherSerial
        self.inventory.launcher = LauncherSerial()

        self.inventory.sequence = ['source', 'verifier']
        
        geometer = self.inventory.geometer
        self.inventory.geometer.inventory.source = (0,0,0), (0,0,0)
        self.inventory.geometer.inventory.verifier = (0,0,0), (0,0,0)

        storage = self.inventory.source
        #the path where neutrons were saved in the simulation
        #of Instrument1
        path = os.path.join(instrument1_outputpath, neutron_storage_path )
        storage.inventory.path = path
        return
    
    pass # end of Instrument2



class TestCase(unittest.TestCase):


    def test0(self):
        'prepare'
        import os, shutil
        if os.path.exists( neutron_storage_path ): 
            os.remove( neutron_storage_path )
        return


    def test1(self):
        'neutron --> storage'
        instrument = Instrument1('test1')

        import sys
        save = sys.argv
        sys.argv = [
            '',
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=%s' % instrument1_output,
            '--overwrite-datafiles',
            ]

        instrument.run()
        instrument.run_postprocessing()
        sys.argv = save
        return


    def test2(self):
        'storage --> verifier'
        instrument = Instrument2('test2')
        instrument.testFacility = self

        import sys
        save = sys.argv
        sys.argv = [
            save[0],
            '--ncount=10',
            '--buffer_size=5',
            '--output-dir=%s' % instrument2_output,
            '--overwrite-datafiles',
            ]

        instrument.run()
        instrument.run_postprocessing()
        sys.argv = save
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
