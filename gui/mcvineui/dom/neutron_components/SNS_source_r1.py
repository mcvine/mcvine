# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class SNS_source_r1(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'sns_source_r1'

SNS_source_r1.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SNS_source_r1Table = o2t(SNS_source_r1, {'subclassFrom': NeutronComponentTableBase})
