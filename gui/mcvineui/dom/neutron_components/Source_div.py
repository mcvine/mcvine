# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Source_div(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'source_div'

Source_div.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Source_divTable = o2t(Source_div, {'subclassFrom': NeutronComponentTableBase})
