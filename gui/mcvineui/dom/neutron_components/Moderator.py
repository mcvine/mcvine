# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Moderator(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'moderator'

Moderator.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ModeratorTable = o2t(Moderator, {'subclassFrom': NeutronComponentTableBase})
