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

class TestCase(unittest.TestCase):

    def test1(self):
        from mcni.pyre_components.MonochromaticSource import MonochromaticSource
        source = MonochromaticSource('source')
        source.inventory.energy = 60
        source.inventory.velocity = [0,0,1.]
        source._configure()
        self.assertAlmostEqual(source.velocity[2], 3388.04632683, 1)

        source.inventory.energy = 60
        source.inventory.velocity = [1,0,0.]
        source._configure()
        self.assertAlmostEqual(source.velocity[0], 3388.04632683, 1)

        source.inventory.energy = 0
        source.inventory.velocity = [10,0,0.]
        source._configure()
        self.assertAlmostEqual(source.velocity[0], 10)

        source.inventory.velocity = "10,0,0."
        self.assertAlmostEqual(source.inventory.velocity[0], 10)

        return

    pass # end of TestCase


def main():
    unittest.main()
    return


if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
