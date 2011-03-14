# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Monochromator_flat(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'monochromator_flat'

Monochromator_flat.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Monochromator_flatTable = o2t(Monochromator_flat, {'subclassFrom': NeutronComponentTableBase})
