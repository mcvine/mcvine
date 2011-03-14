# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PSD_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'psd_monitor'

PSD_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PSD_monitorTable = o2t(PSD_monitor, {'subclassFrom': NeutronComponentTableBase})
