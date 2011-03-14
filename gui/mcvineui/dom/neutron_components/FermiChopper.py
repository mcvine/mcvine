# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class FermiChopper(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'fermichopper'

FermiChopper.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
FermiChopperTable = o2t(FermiChopper, {'subclassFrom': NeutronComponentTableBase})
