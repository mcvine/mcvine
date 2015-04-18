Development notes
=================

SNS instruments
---------------
They are in instruments/.

There are now ARCS, SEQUOIA, and HYSPEC.

ARCS and SEQUOIA were built earlier, and was translated from mcstas
instrument to pyre script mostly by hand.

HYSPEC app was built by using a different approach.
First the mcstas instrument was modified slightly by translating
the c code at the intialize section to python, and then the mcstas
instrument is compiled into a mcvine application and an accompanying
configuratoin script.
This approach probably should be favored in the long run.


After a beam simulation, a beam analysis is carried out.
ARCS and SEQUOIA has its own script for that, but they are really 
not different form each other.

Generic beam analyzer script: mcvine_analyze_beam
Make sure to set position of source and monitor correctly.


Nexus
"""""

Simulation nexus outputs are created using templates derived from experimental
nexus files.

ARCS: arcs-neutrons2nxs
SEQUOIA: sequoia-neutrons2nxs
HYSPEC and others: mcvine-sns-neutrons2nxs (instruments/SNS/bin)


Add an instrument
"""""""""""""""""

This is a quick guide. not very well organized.

* convert mcstas instrument to python scripts (see script "convert" in HYSPEC/resources)
* add a high-level script <instrument>-beam that runs the beam and do beam analysis
* convert mantid instrument xml file for the instrument to a mcvine instrument, by add an instrument factory to the instrument package


xml parsing
-----------
is done in several layers.

* sampleassembly: sampleassembly.saxml package


geometry
--------
sampleassembly.xml

Geometry information is registered into a registry.
Later when needed, positional and orientational
information of an object can be requested from the registry.

For example, in mccomponents.sample.sampleassembly_support.onSampleAssembly,
calls

 lg.position(scatterer)
 lg.orientation(scatterer)

request the position and orientation of the scatterer.

