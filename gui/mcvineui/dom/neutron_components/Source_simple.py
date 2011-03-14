# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Source_simple(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'source_simple'

Source_simple.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Source_simpleTable = o2t(Source_simple, {'subclassFrom': NeutronComponentTableBase})
