# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Source_gen(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'source_gen'

Source_gen.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Source_genTable = o2t(Source_gen, {'subclassFrom': NeutronComponentTableBase})
