# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Mirror(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'mirror'

Mirror.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
MirrorTable = o2t(Mirror, {'subclassFrom': NeutronComponentTableBase})
