# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class NDMonitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'ndmonitor'

NDMonitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
NDMonitorTable = o2t(NDMonitor, {'subclassFrom': NeutronComponentTableBase})
