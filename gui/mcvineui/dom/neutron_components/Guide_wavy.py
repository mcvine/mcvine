# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Guide_wavy(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'guide_wavy'

Guide_wavy.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Guide_wavyTable = o2t(Guide_wavy, {'subclassFrom': NeutronComponentTableBase})
