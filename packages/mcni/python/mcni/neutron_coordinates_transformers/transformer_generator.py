#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao Lin
#                        California Institute of Technology
#                        (C) 2005-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
factory method to create a transformer.

Please read AbstractNeutronCoordinatesTransformer 
to see the requirements for "convention" and "binding".
'''


def generateTransformer( convention, binding ):
    return generateTransformerClass( convention, binding )()


def generateTransformerClass( convention, binding ):
    from .AbstractNeutronCoordinatesTransformer import AbstractNeutronCoordinatesTransformer as base
    class _(base):

        relativePositionOrientation = staticmethod(convention.relativePositionOrientation)

        applyOffsetRotation = staticmethod(binding.applyOffsetRotation)

        pass #

    return _


# version
__id__ = "$Id$"

#  End of file 
