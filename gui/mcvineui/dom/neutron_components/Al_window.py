# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Al_window(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'al_window'

Al_window.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
Al_windowTable = o2t(Al_window, {'subclassFrom': NeutronComponentTableBase})
