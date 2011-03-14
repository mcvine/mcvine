# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class DivPos_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'divpos_monitor'

DivPos_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
DivPos_monitorTable = o2t(DivPos_monitor, {'subclassFrom': NeutronComponentTableBase})
