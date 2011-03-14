# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Guide(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'guide'

Guide.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
GuideTable = o2t(Guide, {'subclassFrom': NeutronComponentTableBase})
