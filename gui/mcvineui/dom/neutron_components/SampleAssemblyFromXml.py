# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class SampleAssemblyFromXml(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'sampleassemblyfromxml'

SampleAssemblyFromXml.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
SampleAssemblyFromXmlTable = o2t(SampleAssemblyFromXml, {'subclassFrom': NeutronComponentTableBase})
