#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2011  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


# context for mc simulation of a neutron instrument


class SimulationContext:

    def __init__(self, multiple_scattering=False, tracer=None, iteration_no=None):
        self.multiple_scattering = multiple_scattering
        self.tracer = tracer
        self.iteration_no = iteration_no
        return



# version
__id__ = "$Id$"

#  End of file 
