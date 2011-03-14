# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Divergence_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'divergence_monitor'

Divergence_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Divergence_monitorTable = o2t(Divergence_monitor, {'subclassFrom': NeutronComponentTableBase})
