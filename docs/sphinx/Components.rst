.. _Components:

Components
==========


Generic components provided by MCViNE
-------------------------------------

Neutron storage
^^^^^^^^^^^^^^^

In mcvine, you can save neutrons to a neutron storage, and
reuse it in later simulations.

Following components are created for this purpose:

* NeutronFromStorage: retrieve neutrons from a storage and send them running
* NeutronToStorage: save neutrons in simulation to a storage

Example usages
""""""""""""""

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

Error propagation when using neutron storage
""""""""""""""""""""""""""""""""""""""""""""

When we use neutron storage, we need to make sure the
neutrons saved in the storage have enough statistics
for the simulations that use the storage to be successful.

As discussed in :ref:`fundamentals-errorbar-errorprop`, 
the error bar of simulated intensity of a simulation using neutron storage
is given by

.. math::
   Err^2(I) = \Delta^2_{intrinsic} \times I^2  + \sum{p_i^2}

and the instrinsic error induced by using the neutron
storage could be approximated from the data of the simulation
that generated the neutron storage:

.. math::
   \Delta^2_{instrinsic} = \sum p_{ns, i}^2 / (\sum p_{ns, i})^2

where the subscript ":math:`ns`" denotes the simulation that generates
the neutron storage.

You can see that the errobar of a simulation involves a neutron
source that replays neutrons in a neutron storage is limited by
the error bar of the simulation that leads to the neutron storage.
So the rule of thumb of using neutron storage is that
it is necessary to make sure to have a reasonably good statistics 
for the simulation of the neutron storage before using it for
other simulations.


Tools
"""""

Count neutrons in a storage -- "mcvine-neutron-storage-count-neutrons"
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Signature::

 $ mcvine-neutron-storage-count-neutrons <neutron-file>

- Input: a neutron file
- Output: Number of neutrons in the given storage


Compute total intensity in a storage -- "mcvine-neutron-storage-total-intensity"
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Signature::

 $ mcvine-neutron-storage-total-intensity <neutron-file>

- Input: a neutron file
- Output: Total neutron intensity in the given storage


Merge neutron storages -- "mcvine-neutron-storage-merge"
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Signature::
 
 $ mcvine-neutron-storage-merge \ \
     -files=<neutron-files-to-merge> \
     -output=<output-neutron-file>

- Input: neutron file(s)
- Output: merged neutron file



McStas component librarry
-------------------------

.. _user-defined-mcstas-components:

User-defined mcstas components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is not unusual that a user wants to use a mcstas component he 
writes himself. To use a user-defined mcstas component, run::

 $ mcvine-compile-mcstas-component --filename=<user-defined-component-file> --category=<category.>

Here, <user-defined-component-file> is the path to the mcstas component file
you created, <category> is the category this component belongs to.
For example::

 $ mcvine-compile-mcstas-component --filename=Al_window.comp --category=optics

and mcvine will start compiling the component and put it into the system.
If the compiling failed, please don't hesitate to post your questions
to mcvine-users@googlegroups.com 

If everything goes smoothly, now you can use this component just like any other components::

 $ mcvine-component-info --type=Al_window



