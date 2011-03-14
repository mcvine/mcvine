# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Alex Dementsov
#                      California Institute of Technology
#                        (C) 2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from AbstractNeutronComponent import AbstractNeutronComponent as base
class Arm(base):
    abstract = False
    def customizeLubanObjectDrawer(self, drawer):
        # drawer.mold.sequence = ['componentname', 'short_description', 'referencename', 'position', 'orientation']
        drawer.mold.sequence = ['componentname']

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = 'arm'

Arm.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
ArmTable = o2t(Arm, {'subclassFrom': NeutronComponentTableBase})


__date__ = "$Mar 7, 2011 11:49:02 AM$"


