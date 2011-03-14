# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Fermi_chop2(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'fermi_chop2'

Fermi_chop2.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Fermi_chop2Table = o2t(Fermi_chop2, {'subclassFrom': NeutronComponentTableBase})
