
from .transformer_generator import generateTransformer
from mcni.bindings import get as getBinding
from . import mcstas
boostpython = getBinding('BoostPython')
transformer = generateTransformer( mcstas, boostpython )

