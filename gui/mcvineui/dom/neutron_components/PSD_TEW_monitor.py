# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PSD_TEW_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'psd_tew_monitor'

PSD_TEW_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PSD_TEW_monitorTable = o2t(PSD_TEW_monitor, {'subclassFrom': NeutronComponentTableBase})
