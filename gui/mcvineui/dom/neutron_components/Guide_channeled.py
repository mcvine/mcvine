# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Guide_channeled(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'guide_channeled'

Guide_channeled.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Guide_channeledTable = o2t(Guide_channeled, {'subclassFrom': NeutronComponentTableBase})
