# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class DiskChopper(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'diskchopper'

DiskChopper.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
DiskChopperTable = o2t(DiskChopper, {'subclassFrom': NeutronComponentTableBase})
