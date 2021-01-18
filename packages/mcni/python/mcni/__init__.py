#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2018  All Rights Reserved
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


def simulate( 
    instrument, geometer, neutrons, 
    simulator = None, 
    context = None,
    **kwds
    ):
    
    '''run a simulation of the given instrument

    instrument: a neutron instrument
    geometer: a geometer that contains geometry info of components in the instrument
    neutrons: a container of neutrons
    simulator: the simulation driver

    context: the context of the simulation
    '''
    if context is None:
        from .SimulationContext import SimulationContext
        context = SimulationContext()
        for k, v in kwds.items():
            setattr(context, k, v)
            continue
        
    if simulator is None:
        from .instrument_simulator import default_simulator
        simulator = default_simulator
        pass
    return simulator.run( 
        neutrons, instrument, geometer, 
        context = context)


def run_ppsd(path):
    "run postprocessing scripts in the given path"
    import glob, sys, os
    scripts = glob.glob(os.path.join(path, '*.py'))
    for script in scripts:
        cmd = '%s %s' % (sys.executable, script)
        _exec(cmd)
        continue
    return
def _exec(cmd):
    import os
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)
    return


def run_ppsd_in_parallel(path, nodes):
    "run postprocessing scripts in the given path in parallel using MPI"
    import glob, sys, os
    scripts = glob.glob(os.path.join(path, '*.py'))
    for script in scripts:
        cmd = 'mpirun -np %s %s %s' % (nodes, sys.executable, script)
        _exec(cmd)
        continue
    return    


def geometer( *args, **kwds ):
    'factory constructs a geometer'
    from .Geometer import Geometer
    return Geometer( *args, **kwds )


def instrument( *args, **kwds ):
    'create an instrument that is a container of neutron components'
    from .Instrument import Instrument
    return Instrument( *args, **kwds )


def findcomponentfactory(*args, **kwds):
    '''find a component factory given its type name, category name, and/or supplier name
    
    findcomponentfactory(type="MonochromaticSource")
    findcomponentfactory(type="MonochromaticSource", category="sources")
    findcomponentfactory(type="MonochromaticSource", supplier="mcni")
    findcomponentfactory(type="MonochromaticSource", category="sources", supplier="mcni")
    '''
    from ._find_component import find
    type, category, supplier = find(*args, **kwds)
    return componentfactory(type=type, category=category, supplier=supplier)


# mcvine wrapper of journal
from ._journal import journal

__all__ = [
    'simulate',
    'geometer',
    'instrument',
    'journal',
    ]


from .bindings import current as binding
cpp_instance_factories = [
    'neutron_buffer',
    'position',
    'velocity',
    'spin',
    'state',
    'neutron',
    'vector3',
    ]
for method in cpp_instance_factories:
    exec('%s = binding.%s' % (method, method))
    continue
__all__ += cpp_instance_factories


from ._component_factories import *
from ._component_factories import __all__ as t
__all__ += t; del t


from ._component_listing import *
from ._component_listing import __all__ as t
__all__ += t; del t


# version
__id__ = "$Id$"

#  End of file 
