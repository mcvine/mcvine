
from AbstractNeutronCoordinatesTransformer import AbstractNeutronCoordinatesTransformer as base
class Transformer_McStas_BP(base):

    from mcstas import relativePositionOrientation
    relativePositionOrientation = staticmethod(relativePositionOrientation)
    
    from boostpython import applyOffsetRotation
    applyOffsetRotation = staticmethod(applyOffsetRotation)

    pass # end of Transformer_McStas_BP

transformer_McStas_BP = Transformer_McStas_BP()

