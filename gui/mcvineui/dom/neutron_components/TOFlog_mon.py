# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOFlog_mon(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'toflog_mon'

TOFlog_mon.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOFlog_monTable = o2t(TOFlog_mon, {'subclassFrom': NeutronComponentTableBase})
