# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOF2E_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'tof2e_monitor'

TOF2E_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOF2E_monitorTable = o2t(TOF2E_monitor, {'subclassFrom': NeutronComponentTableBase})
