import os
import mcvine, mcvine.components
instrument = mcvine.instrument()
# add source
source = mcvine.components.sources.Source_simple('source')
instrument.append(source, position=(0,0,0))
# add sample
sample = mcvine.components.samples.V_sample('sample')
instrument.append(sample, position=(0,0,1))
# add detector system
from mcvine import resources
arcsxml = os.path.join(
    resources.instrument('ARCS'), 'detsys', 'ARCS.xml.fornxs')
ds = mcvine.components.detectors.DetectorSystemFromXml('ds', instrumentxml=arcsxml, outfilename='events.dat')
instrument.append(ds, position=(0,0,1))
