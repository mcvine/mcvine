#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

def copyright():
    return "mcni pyre module: Copyright (c) 2007 Jiao Lin";


def simulate( instrument, geometer, neutrons, simulator = None ):
    if simulator is None:
        from instrument_simulator import default_simulator
        simulator = default_simulator
        pass
    return simulator.run( neutrons, instrument, geometer )


def geometer( *args, **kwds ):
    from Geometer import Geometer
    return Geometer( *args, **kwds )


def instrument( *args, **kwds ):
    from Instrument import Instrument
    return Instrument( *args, **kwds )



from bindings import current as binding
cpp_instance_factories = [
    'neutron_buffer',
    'position',
    'velocity',
    'spin',
    'state',
    'neutron',
    ]
for method in cpp_instance_factories:
    exec '%s = binding.%s' % (method, method)
    continue


from _component_factories import *
from _component_listing import *


# version
__id__ = "$Id$"

#  End of file 
