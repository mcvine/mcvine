# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Filter_gen(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'filter_gen'

Filter_gen.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Filter_genTable = o2t(Filter_gen, {'subclassFrom': NeutronComponentTableBase})
