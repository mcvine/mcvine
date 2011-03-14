# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Arm(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'arm'

Arm.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ArmTable = o2t(Arm, {'subclassFrom': NeutronComponentTableBase})



