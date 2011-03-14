# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class IQE_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'iqe_monitor'

IQE_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
IQE_monitorTable = o2t(IQE_monitor, {'subclassFrom': NeutronComponentTableBase})
