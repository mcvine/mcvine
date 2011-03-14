# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class ESS_moderator_long(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'ess_moderator_long'

ESS_moderator_long.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ESS_moderator_longTable = o2t(ESS_moderator_long, {'subclassFrom': NeutronComponentTableBase})
