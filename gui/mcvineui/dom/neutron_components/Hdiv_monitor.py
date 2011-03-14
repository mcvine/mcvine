# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Hdiv_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'hdiv_monitor'

Hdiv_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Hdiv_monitorTable = o2t(Hdiv_monitor, {'subclassFrom': NeutronComponentTableBase})
