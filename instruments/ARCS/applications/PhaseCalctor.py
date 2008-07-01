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


class PhaseCalctor:

    def phase( self, distance ):
        return distance/self.vel+self.t0
    

    def __init__(self, neutron_energy):
        from mcni.utils import e2v
        self.t0 = self.__calc_t0(neutron_energy)
        self.vel = e2v(neutron_energy)
        

    def __calc_t0(self, neutron_energy):
        from numpy import pi as PI, log10, tanh, sqrt, floor
        ch_x=log10(neutron_energy);
        ch_y=-0.45*ch_x*(1+tanh((ch_x+1.2)/0.38))/2
        ch_y-=0.13*ch_x*(1-tanh((ch_x+1.2)/0.38))/2
        ch_y-=0.35*tanh((ch_x+1.2)/0.38)-0.51; # proton hit -- a few microseconds -- nentron emission. ch_y: fit function?. toffset -- ch_y converted back to time
        t0=pow(10,ch_y)/1.0e6;
        return t0
    

# version
__id__ = "$Id: PhaseCalctor.py 644 2007-09-29 15:30:06Z linjiao $"

# Generated automatically by PythonMill on Sun May  8 14:02:50 2005

# End of file 
