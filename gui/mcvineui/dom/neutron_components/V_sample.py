# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class V_sample(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'v_sample'

V_sample.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
V_sampleTable = o2t(V_sample, {'subclassFrom': NeutronComponentTableBase})
