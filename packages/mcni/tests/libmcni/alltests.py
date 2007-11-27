#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#              (C) 2005 All Rights Reserved  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest
import journal


def main():
    from vector_TestCase import pysuite
    vectorSuite = pysuite()

    from Functor_TestCase import pysuite
    FunctorSuite = pysuite()

    from rootfinding_TestCase import pysuite
    rootfindingSuite = pysuite()

    alltests = unittest.TestSuite( (vectorSuite, FunctorSuite, rootfindingSuite) )
    unittest.TextTestRunner(verbosity=2).run(alltests)


if __name__ == "__main__":
    main()

# version
__id__ = "$Id: alltests.py 534 2006-04-23 05:55:33Z jiao $"

# End of file 
