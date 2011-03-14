# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Guide_gravity(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'guide_gravity'

Guide_gravity.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Guide_gravityTable = o2t(Guide_gravity, {'subclassFrom': NeutronComponentTableBase})
