# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PSDcyl_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'psdcyl_monitor'

PSDcyl_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PSDcyl_monitorTable = o2t(PSDcyl_monitor, {'subclassFrom': NeutronComponentTableBase})
