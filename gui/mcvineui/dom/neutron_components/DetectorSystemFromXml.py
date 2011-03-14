# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class DetectorSystemFromXml(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'detectorsystemfromxml'

DetectorSystemFromXml.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
DetectorSystemFromXmlTable = o2t(DetectorSystemFromXml, {'subclassFrom': NeutronComponentTableBase})
