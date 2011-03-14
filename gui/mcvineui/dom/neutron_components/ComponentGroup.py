# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class ComponentGroup(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'componentgroup'

ComponentGroup.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ComponentGroupTable = o2t(ComponentGroup, {'subclassFrom': NeutronComponentTableBase})
