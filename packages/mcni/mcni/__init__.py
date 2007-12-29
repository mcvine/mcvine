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


def neutron_buffer( n ):
    from mcni.mcnibp import NeutronEventBuffer
    return NeutronEventBuffer( n )


def position( x,y,z ):
    from mcni.mcnibp import Position_double
    return Position_double( x,y,z )


def velocity( x,y,z ):
    from mcni.mcnibp import Velocity_double
    return Velocity_double( x,y,z )


def spin(s1, s2):
    from mcni.mcnibp import NeutronSpin
    return NeutronSpin( s1, s2 )


def state(r = (0,0,0), v = (0,0,3000), s = (0,1)):
    from mcni.mcnibp import NeutronState
    return NeutronState( position( *r ), velocity( *v ), spin( *s ) )


def neutron(r = (0,0,0), v = (0,0,3000), s = (0,1), time = 0, prob = 1.):
    from mcni.mcnibp import NeutronEvent
    return NeutronEvent(state(r,v,s), time, prob)


def _import_bindings():
    import mcnibp
    return

_import_bindings()


# version
__id__ = "$Id$"

#  End of file 
