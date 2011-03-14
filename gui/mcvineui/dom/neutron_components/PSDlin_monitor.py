# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PSDlin_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'psdlin_monitor'

PSDlin_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PSDlin_monitorTable = o2t(PSDlin_monitor, {'subclassFrom': NeutronComponentTableBase})
