#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 


"""
This package is the base of mcvine.
It provides the most fundamental data objects for Monnte Carlo simulation
of neutron instruments, such as neutron, instrument, and component.
It also implements a Monte Carlo simulator.
"""


def copyright():
    return "mcni pyre module: Copyright (c) 2006-2010 Jiao Lin";


def simulate( instrument, geometer, neutrons, simulator = None, multiple_scattering=False):
    '''run a simulation of the given instrument

    instrument: a neutron instrument
    geometer: a geometer that contains geometry info of components in the instrument
    neutrons: a container of neutrons
    simulator: the simulation driver
    '''
    if simulator is None:
        from instrument_simulator import default_simulator
        simulator = default_simulator
        pass
    return simulator.run( neutrons, instrument, geometer, multiple_scattering=multiple_scattering)


def geometer( *args, **kwds ):
    'factory constructs a geometer'
    from Geometer import Geometer
    return Geometer( *args, **kwds )


def instrument( *args, **kwds ):
    'create an instrument that is a container of neutron components'
    from Instrument import Instrument
    return Instrument( *args, **kwds )


__all__ = [
    'simulate',
    'geometer',
    'instrument',
    ]


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
__all__ += cpp_instance_factories


from _component_factories import *
from _component_factories import __all__ as t
__all__ += t; del t


from _component_listing import *
from _component_listing import __all__ as t
__all__ += t; del t


# version
__id__ = "$Id$"

#  End of file 
