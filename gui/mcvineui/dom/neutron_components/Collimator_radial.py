# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Collimator_radial(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'collimator_radial'

Collimator_radial.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Collimator_radialTable = o2t(Collimator_radial, {'subclassFrom': NeutronComponentTableBase})
