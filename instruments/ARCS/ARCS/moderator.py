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


def estimate_emission_time(neutron_energy):
    
    """compute emission time for a given neutron energy

    neutron_energy: unit meV
    """

    # The implementation here is taken from Garrett's
    # mcstas simulation code.
    
    from numpy import pi as PI, log10, tanh, sqrt, floor
    ch_x=log10(neutron_energy);
    ch_y=-0.45*ch_x*(1+tanh((ch_x+1.2)/0.38))/2
    ch_y-=0.13*ch_x*(1-tanh((ch_x+1.2)/0.38))/2
    ch_y-=0.35*tanh((ch_x+1.2)/0.38)-0.51; # proton hit -- a few microseconds -- nentron emission. ch_y: fit function?. toffset -- ch_y converted back to time
    t0=pow(10,ch_y)/1.0e6;
    return t0
    

# version
__id__ = "$Id$"

# End of file 
