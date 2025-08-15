#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



import unittestX as unittest


from mcni.AbstractComponent import AbstractComponent
class C( AbstractComponent ):

    def __init__(self):
        self.count = 0

    def process(self, neutrons):
        self.count = len(neutrons)
        return neutrons
    

# dummy geometer
class Geometer(object):

    def position(self, c): return (0,0,0)
    def orientation(self, c): return (0,0,0)




class SetNeutron(AbstractComponent):

    def process(self, neutrons):
        from mcni import neutron
        for i in range(len(neutrons)):
            neutrons[i] = neutron(v=(0,0,1))
            continue
        return


class SaveNeutron(AbstractComponent):


    def __init__(self):
        self.neutron = None


    def process(self, neutrons):
        n0 = neutrons[0]
        from mcni import neutron
        self.neutron = neutron(
            r=n0.state.position, v=n0.state.velocity, 
            s=(n0.state.spin.s1,n0.state.spin.s2),
            time=n0.time,
            prob=n0.probability,
            )
        return


    
class TestCase(unittest.TestCase):


    def test0(self):
        'ComponentGroup'
        comps = [C() for i in range(10)]
        geometer = Geometer()
        from mcni.neutron_coordinates_transformers import default as transformer
        from mcni.components.ComponentGroup import ComponentGroup
        cg = ComponentGroup('cg', comps, geometer, transformer)
        import mcni
        b = mcni.neutron_buffer(10)
        cg.process(b)
        for c in comps:
            self.assertEqual(c.count, 10)
            continue
        return


    def test1(self):
        'ComponentGroup: geometer'
        # components
        c1 = SaveNeutron()
        comps = [c1]
        # geometer
        from mcni.Geometer import Geometer
        geometer = Geometer()
        geometer.register(c1, (0,0,1), (0,90,0))
        #
        from mcni.neutron_coordinates_transformers import default as transformer
        from mcni.components.ComponentGroup import ComponentGroup
        cg = ComponentGroup('cg', comps, geometer, transformer)
        import mcni
        b = mcni.neutron_buffer(1)
        SetNeutron('set').process(b)
        cg.process(b)
        # print c1.neutron
        self.assertVectorAlmostEqual(c1.neutron.state.position, (1,0,0))
        self.assertVectorAlmostEqual(c1.neutron.state.velocity, (-1,0,0))
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
