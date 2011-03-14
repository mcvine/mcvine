# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class MonochromaticSource(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'monochromaticsource'

MonochromaticSource.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
MonochromaticSourceTable = o2t(MonochromaticSource, {'subclassFrom': NeutronComponentTableBase})
