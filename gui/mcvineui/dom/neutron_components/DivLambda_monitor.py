# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class DivLambda_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'divlambda_monitor'

DivLambda_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
DivLambda_monitorTable = o2t(DivLambda_monitor, {'subclassFrom': NeutronComponentTableBase})
