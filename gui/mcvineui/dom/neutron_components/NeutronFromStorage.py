# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class NeutronFromStorage(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'neutronfromstorage'

NeutronFromStorage.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
NeutronFromStorageTable = o2t(NeutronFromStorage, {'subclassFrom': NeutronComponentTableBase})
