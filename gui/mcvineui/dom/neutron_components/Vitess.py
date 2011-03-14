# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Vitess(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'vitess'

Vitess.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
VitessTable = o2t(Vitess, {'subclassFrom': NeutronComponentTableBase})
