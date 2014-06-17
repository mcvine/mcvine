Development notes
=================

SNS instruments
---------------
They are in instruments/.

There are now ARCS, SEQUOIA, and HYSPEC.

ARCS and SEQUOIA were built earlier, and was translated from mcstas
instrument to pyre script mostly by hand.

HYSPEC was done by using a different approach.
First the mcstas instrument was modified slightly by translating
the c code at the intialize section to python, and then the mcstas
instrument is compiled into a mcvine application and an accompanying
configuratoin script.
This approach probably should be favored in the long run.


After a beam simulation, a beam analysis is carried out.
ARCS and SEQUOIA has its own script for that, but they are really 
not different form each other.
Should create a generic script for that.


Nexus
"""""

Simulation nexus outputs are created using templats derived from experimental
nexus files.


