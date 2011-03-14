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


def factory(Component, **kwds):
    import luban.orm
    base = luban.orm.object2actor(Component, **kwds)
    from NeutronComponentOrmActorMixin import NeutronComponentOrmActorMixin
    class Actor(NeutronComponentOrmActorMixin, base): 

        def _postStoringUserInputs(self, director):
        
            action1 = super(Actor, self)._postStoringUserInputs(director)
            refresh_component_button = self._actionToRefreshComponentButtonInComponentChain(director)
            return [action1, refresh_component_button]

    return Actor
 

# version
__id__ = "$Id$"

# End of file 
