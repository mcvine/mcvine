# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class NeutronToStorage(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'neutrontostorage'

NeutronToStorage.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
NeutronToStorageTable = o2t(NeutronToStorage, {'subclassFrom': NeutronComponentTableBase})
