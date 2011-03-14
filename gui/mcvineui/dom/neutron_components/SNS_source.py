# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class SNS_source(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'sns_source'

SNS_source.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SNS_sourceTable = o2t(SNS_source, {'subclassFrom': NeutronComponentTableBase})
