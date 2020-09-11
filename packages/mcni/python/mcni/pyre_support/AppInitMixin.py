#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# Mixin to alter pyre app behavior on initialization


from .ComponentInitMixin import ComponentInitMixin
class AppInitMixin(ComponentInitMixin):


    def _init_before_my_inventory(self):
        # go over all sub-components and see if any of them is requested 
        # for help
        requested = self._showHelpOnly or _requestedForHelp_r(self)
        # if yes, 
        # need to let all my descendents know
        if requested:
            _setShowHelpOnly_r(self)
        return


    pass # end of ComponentInitMixin


def _setShowHelpOnly_r(comp):
    'set _showHelpOnly to True recursively'
    comp._showHelpOnly = True
    for c in comp.components():
        _setShowHelpOnly_r(c)
        continue
    return


def _requestedForHelp_r(component):
    "check if a component or its subcomponent is requested for help"
    if _requestedForHelp(component):
        return True
    for comp in component.components():
        if _requestedForHelp_r(comp):
            return True
        continue
    return False


def _requestedForHelp(component):
    "check if a component is requested for help"
    return component.inventory.usage or \
        component.inventory.showProperties or \
        component.inventory.showComponents or \
        component.inventory.showCurator


# version
__id__ = "$Id$"

# End of file 
