# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class NeutronPrinter(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'neutronprinter'

NeutronPrinter.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
NeutronPrinterTable = o2t(NeutronPrinter, {'subclassFrom': NeutronComponentTableBase})
