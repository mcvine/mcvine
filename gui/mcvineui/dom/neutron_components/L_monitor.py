# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class L_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'l_monitor'

L_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
L_monitorTable = o2t(L_monitor, {'subclassFrom': NeutronComponentTableBase})
