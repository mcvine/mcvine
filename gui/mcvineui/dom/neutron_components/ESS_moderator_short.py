# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class ESS_moderator_short(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'ess_moderator_short'

ESS_moderator_short.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ESS_moderator_shortTable = o2t(ESS_moderator_short, {'subclassFrom': NeutronComponentTableBase})
