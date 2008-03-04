

def generateTransformer( convention, binding ):
    return generateTransformerClass( convention, binding )()


def generateTransformerClass( convention, binding ):
    from AbstractNeutronCoordinatesTransformer import AbstractNeutronCoordinatesTransformer as base
    class _(base):

        relativePositionOrientation = staticmethod(convention.relativePositionOrientation)

        applyOffsetRotation = staticmethod(binding.applyOffsetRotation)

        pass #

    return _


from mcni.bindings import get as getBinding

import mcstas


boostpython = getBinding('BoostPython')
transformer_McStas_BP = generateTransformer( mcstas, boostpython )


default = transformer_McStas_BP
