eventsdat = 'events.dat'
instrumentxml = 'Pharos.xml'
Ei = 70 #incident energy
Q = 5 #momentum transfer
E = 30 #energy transfer
from mcni.utils import e2v
vi = e2v( Ei ) #m/s

from instrument.nixml import parse_file
instrument = parse_file( instrumentxml )
geometer = instrument.geometer
import mcni.units as units
meter = units.length.meter
mod2sample = geometer.distanceToSample( instrument.getModerator() ) / meter
        
tmin = mod2sample/vi
sample2det = instrument.getDetectorSystem().shape().in_radius
tmax = tmin + sample2det/e2v( 5 )
tofparams = tmin, tmax, (tmax-tmin)/1000

Idpt_filename = 'Idpt.h5'
