#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#



from mcvine.applications.InstrumentBuilder import build
components = ['comp%s' % i for i in range(10)]
InstrumentBase = build(components)

class Instrument(InstrumentBase):

    def main(self):
        import numpy.testing as nt
        from mcni.neutron_coordinates_transformers.mcstasRotations import toMatrix

        geometer = self.inventory.geometer

        comp2pos = geometer.position('comp2')
        nt.assert_array_almost_equal(comp2pos, (1,0,0))

        comp2ori = geometer.orientation('comp2')
        nt.assert_array_almost_equal(comp2ori, (0,0,0))

        comp3pos = geometer.position('comp3')
        nt.assert_array_almost_equal(comp3pos, (1,0,0))

        comp3ori = geometer.orientation('comp3')
        nt.assert_array_almost_equal(comp3ori, toMatrix((3,4,5)))

        comp5ori = geometer.orientation('comp5')
        nt.assert_array_almost_equal(comp5ori, toMatrix((-90,0,90)))

        comp6pos = geometer.position('comp6')
        nt.assert_array_almost_equal(comp6pos, (-2,3,-1))

        return


def main():
    instrument = Instrument('geometer-relative-coords-test1')
    instrument.run()
    return

if __name__ == "__main__": main()
    
# End of file 
