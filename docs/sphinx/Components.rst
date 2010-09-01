.. _Components:

Components
==========

Neutron storage
---------------

In mcvine, you can save neutrons to a neutron storage, and
reuse it in later simulations.

Following components are created for this purpose:

* NeutronFromStorage: retrieve neutrons from a storage and send them running
* NeutronToStorage: save neutrons in simulation to a storage

Example usages
^^^^^^^^^^^^^^

1. Separate simulations of ARCS beam and sample scattering
Simulation of an ARCS experiment can be done in two steps.
The first step is to simulation the neutron component chain 
down to the sample position::

 moderator -> core-vessel-insert -> shutter-guide -> guide-1 ->
   ... -> fermi-chopper -> ... -> guide-5 -> neutron-to-storage

Result of the first simulation step is a data file that contains
all the neutrons reach the sample position.
Those neutrons can be reused in various futher simulations.

For example we can simulate the scattering of neutrons from sample::

 neutron-from-storage -> sample -> arcs-detector-system

We can use different samples in different simulations that all
use the neutrons from the same neutron storage.

We could also put various monitors to examine the neutrons
in the storage::

 neutron-from-storage -> monitor

