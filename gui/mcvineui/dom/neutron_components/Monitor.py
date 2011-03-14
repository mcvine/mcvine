# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'monitor'

Monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
MonitorTable = o2t(Monitor, {'subclassFrom': NeutronComponentTableBase})
