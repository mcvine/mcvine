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



class NeutronComponentOrmActorMixin:


    def _actionToRefreshComponentButtonInComponentChain(self, director):
        # load component
        component = director.clerk.orm(self._load(director))
        
        # action to refresh the button in the cmponent chain
        from mcvineui.visuals.componentchain import \
            button_id_formatter_for_component, createComponentButton
        button_id = button_id_formatter_for_component % self.inventory.id
        newbutton = createComponentButton(component)
        from luban.content import select
        return select(id=button_id).replaceBy(newbutton)
 

# version
__id__ = "$Id$"

# End of file 
