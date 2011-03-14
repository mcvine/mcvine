# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Source_Maxwell_3(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'source_maxwell_3'

Source_Maxwell_3.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Source_Maxwell_3Table = o2t(Source_Maxwell_3, {'subclassFrom': NeutronComponentTableBase})
