# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class E_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'e_monitor'

E_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
E_monitorTable = o2t(E_monitor, {'subclassFrom': NeutronComponentTableBase})
