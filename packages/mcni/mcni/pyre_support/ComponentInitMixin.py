#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# Mixin to alter pyre component behavior on initialization


class ComponentInitMixin(object):

    def init(self):
        # some initialization must be done before my inventory initialize
        self._init_before_my_inventory()
        
        # the following is copied from pyre.inventory.Configurable
        
        # initialize my subcomponents
        self.inventory.init()

        # perform any last initializations
        self._init()

        return
    
        
    def _init_before_my_inventory(self):
        # by default nothing to do
        return


    pass # end of ComponentInitMixin


# version
__id__ = "$Id$"

# End of file 
