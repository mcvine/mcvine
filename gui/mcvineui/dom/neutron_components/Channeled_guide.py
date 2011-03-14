# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Channeled_guide(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'channeled_guide'

Channeled_guide.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Channeled_guideTable = o2t(Channeled_guide, {'subclassFrom': NeutronComponentTableBase})
