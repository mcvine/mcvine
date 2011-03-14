# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class NeutronsOnCone_FixedQE(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'neutronsoncone_fixedqe'

NeutronsOnCone_FixedQE.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
NeutronsOnCone_FixedQETable = o2t(NeutronsOnCone_FixedQE, {'subclassFrom': NeutronComponentTableBase})
