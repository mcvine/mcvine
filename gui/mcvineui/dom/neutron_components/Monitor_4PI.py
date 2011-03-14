# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Monitor_4PI(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'monitor_4pi'

Monitor_4PI.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Monitor_4PITable = o2t(Monitor_4PI, {'subclassFrom': NeutronComponentTableBase})
