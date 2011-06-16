#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2005-2008 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def phase( neutron_energy, moderator2chopper = 18.0, emission_time = None ):
    '''compute phase of fermi chopper
    '''
    
    if emission_time is None:
        from moderator import estimate_emission_time
        emission_time = estimate_emission_time(neutron_energy)
        
    velocity = e2v(neutron_energy)
    
    return moderator2chopper/velocity + emission_time
    

from _utils import e2v


# version
__id__ = "$Id$"

# End of file 
