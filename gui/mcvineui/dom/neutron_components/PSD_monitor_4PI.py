# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PSD_monitor_4PI(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'psd_monitor_4pi'

PSD_monitor_4PI.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PSD_monitor_4PITable = o2t(PSD_monitor_4PI, {'subclassFrom': NeutronComponentTableBase})
