# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Dummy(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'dummy'

Dummy.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
DummyTable = o2t(Dummy, {'subclassFrom': NeutronComponentTableBase})
