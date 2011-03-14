# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Selector(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'selector'

Selector.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SelectorTable = o2t(Selector, {'subclassFrom': NeutronComponentTableBase})
