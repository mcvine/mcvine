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


from mcni.components.RegistryBase import RegistryBase as base


class Registry(base):
    
    def setup_repos(self):
        import repositories
        from repositories import all as repos
        repos = list(repos)
        repos.reverse()
        self.repos = repos
        return



# version
__id__ = "$Id$"

# End of file 
