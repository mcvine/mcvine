# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Single_crystal(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'single_crystal'

Single_crystal.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Single_crystalTable = o2t(Single_crystal, {'subclassFrom': NeutronComponentTableBase})
