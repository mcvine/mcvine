# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class TOF_monitor2(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'tof_monitor2'

TOF_monitor2.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
TOF_monitor2Table = o2t(TOF_monitor2, {'subclassFrom': NeutronComponentTableBase})
