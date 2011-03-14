# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Collimator_linear(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'collimator_linear'

Collimator_linear.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Collimator_linearTable = o2t(Collimator_linear, {'subclassFrom': NeutronComponentTableBase})
