# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Monitor_nD(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'monitor_nd'

Monitor_nD.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Monitor_nDTable = o2t(Monitor_nD, {'subclassFrom': NeutronComponentTableBase})
