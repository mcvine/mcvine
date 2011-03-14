# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class SNS_source4(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'sns_source4'

SNS_source4.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SNS_source4Table = o2t(SNS_source4, {'subclassFrom': NeutronComponentTableBase})
