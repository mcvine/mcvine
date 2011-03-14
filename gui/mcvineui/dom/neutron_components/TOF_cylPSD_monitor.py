# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOF_cylPSD_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'tof_cylpsd_monitor'

TOF_cylPSD_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOF_cylPSD_monitorTable = o2t(TOF_cylPSD_monitor, {'subclassFrom': NeutronComponentTableBase})
