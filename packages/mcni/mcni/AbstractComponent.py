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


class AbstractComponent:


    '''base class of Monte Carlo neutron components'''

    
    def __init__(self, name):
        self.name = name
        return
    
    
    def process(self, neutrons):
        raise NotImplementedError


    pass # AbstractComponent


# version
__id__ = "$Id$"

# End of file 
