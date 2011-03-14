# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Vertical_T0(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'vertical_t0'

Vertical_T0.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Vertical_T0Table = o2t(Vertical_T0, {'subclassFrom': NeutronComponentTableBase})
