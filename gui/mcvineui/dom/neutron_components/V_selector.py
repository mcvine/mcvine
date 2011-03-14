# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class V_selector(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'v_selector'

V_selector.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
V_selectorTable = o2t(V_selector, {'subclassFrom': NeutronComponentTableBase})
