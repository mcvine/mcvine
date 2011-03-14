# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class CNCS_radial_coll(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'cncs_radial_coll'

CNCS_radial_coll.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
CNCS_radial_collTable = o2t(CNCS_radial_coll, {'subclassFrom': NeutronComponentTableBase})
