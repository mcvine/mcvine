# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from luban.applications.UIApp import UIApp as base


class ScriptBase(base):


    class Inventory(base.Inventory):

        import pyre.inventory


    def _getPrivateDepositoryLocations(self):
        return ['../config', '../content/components', '/tmp/luban-services']



# version
__id__ = "$Id$"

# End of file 
