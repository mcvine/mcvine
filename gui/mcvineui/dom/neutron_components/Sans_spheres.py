# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Sans_spheres(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'sans_spheres'

Sans_spheres.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Sans_spheresTable = o2t(Sans_spheres, {'subclassFrom': NeutronComponentTableBase})
