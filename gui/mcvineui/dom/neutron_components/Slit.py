# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Slit(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'slit'

Slit.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SlitTable = o2t(Slit, {'subclassFrom': NeutronComponentTableBase})
