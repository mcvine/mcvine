# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class PowderN(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'powdern'

PowderN.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
PowderNTable = o2t(PowderN, {'subclassFrom': NeutronComponentTableBase})
