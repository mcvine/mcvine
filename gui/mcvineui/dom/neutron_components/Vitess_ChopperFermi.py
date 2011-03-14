# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Vitess_ChopperFermi(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'vitess_chopperfermi'

Vitess_ChopperFermi.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Vitess_ChopperFermiTable = o2t(Vitess_ChopperFermi, {'subclassFrom': NeutronComponentTableBase})
