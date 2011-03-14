# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOF_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'tof_monitor'

TOF_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOF_monitorTable = o2t(TOF_monitor, {'subclassFrom': NeutronComponentTableBase})
