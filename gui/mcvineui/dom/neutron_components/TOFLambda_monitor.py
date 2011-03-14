# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOFLambda_monitor(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'toflambda_monitor'

TOFLambda_monitor.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOFLambda_monitorTable = o2t(TOFLambda_monitor, {'subclassFrom': NeutronComponentTableBase})
