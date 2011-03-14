# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Bender(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'bender'

Bender.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
BenderTable = o2t(Bender, {'subclassFrom': NeutronComponentTableBase})
