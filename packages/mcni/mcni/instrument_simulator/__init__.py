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


## Note:
##   1. This package depends on dsm

def copyright():
    return "mcni.instrument_simulators module: Copyright (c) 2007 Jiao Lin";


def simulator_McStas_BP( ):
    from AbstractInstrumentSimulator import AbstractInstrumentSimulator as base
    from mcni.neutron_coordinates_transformers import transformer_McStas_BP
    class Simulator(base):
        neutron_coordinates_transformer = transformer_McStas_BP
        pass
    return Simulator()


default_simulator = simulator_McStas_BP()


# version
__id__ = "$Id$"

#  End of file 
