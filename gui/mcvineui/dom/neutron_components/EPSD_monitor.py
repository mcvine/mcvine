# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class EPSD_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'epsd_monitor'

EPSD_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
EPSD_monitorTable = o2t(EPSD_monitor, {'subclassFrom': NeutronComponentTableBase})
