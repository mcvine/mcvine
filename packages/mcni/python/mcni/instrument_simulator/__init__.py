#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 2006-2010  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


## Note:
##   1. This package depends on dsm

def copyright():
    return "mcni.instrument_simulators module: Copyright (c) 2006-2010 Jiao Lin";


def simulator(neutron_coordinates_transformer):
    t = neutron_coordinates_transformer
    from AbstractInstrumentSimulator import AbstractInstrumentSimulator as base
    class Simulator(base):
        neutron_coordinates_transformer = t
        pass
    return Simulator()


from mcni.neutron_coordinates_transformers import default as default_neutron_coordinates_transformer
default_simulator = simulator( default_neutron_coordinates_transformer )


# version
__id__ = "$Id$"

#  End of file 
