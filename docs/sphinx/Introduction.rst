Introduction
==============

To put it simple, MCViNE is a Monte Carlo simulation framework 
useful for simulating neutron experiments. 

1. MCViNE is a framework to construct simulated neutron instruments, and manage the flow of neutrons through them from moderator to detector.
2. It also provides a mechanism to allow users to assemble a complex sample component (including sample and also the sample environment, eg. sample holder). This mechanism is extensible to handle arbitrary complex geometeric shapes of neutron scatterer, and arbitrary complex physics of neutron scattering.

A natural question to ask is, how is it different from existing legacy Monte Carlo
neutron scattering code such as mcstas, vitess, etc?
Please take a moment to read :ref:`philosophy of MCViNE <philosophy>`.


.. _overview:

Overview
--------

Currently MCViNE software is only available for the Linux platform,
which was selected because other tools for scientific computing, including
molecular dynamics and ab initio simulations, use this platform.
Detailed installation instructions for MCViNE are available at
:ref:`Installation <installation>`.
Building the source is driven by a python script, but the underlying
build engine is based on gnu make.

.. usages of instrument simulation applications, 

The MCViNE :ref:`user documentation <mcvinedocs>` includes
:ref:`explanations of MCViNE concepts <philosophy>`,
:ref:`tutorials <tutorials>`, 
:ref:`usage of neutron components <Components>`,
and
:ref:`instructions for creating a sample assembly <SampleAssembly>`.

At this point, MCViNE is under the subversion (svn) version control system,
and anonymous svn access is available at svn://danse.us/MCViNE.
MCViNE source code is available for online-browsing at 
`the trac site <http://danse.us/trac/MCViNE>`_.

MCViNE is currently deployed on the analysis computing clusters at the
Spallation Neutron Source (SNS).
Any SNS user can use MCViNE at analysis.sns.gov after running an
environment setup script.

There are many functionalities available in the MCViNE package, 
so novice users may find it difficult to navigate through the user
documentation and learn how to perform MCViNE simulations for their needs.
To make MCViNE more readily accessible to non-expert users,
we are experimenting with 
:ref:`workflow templates <workflows>`.
Users can easily clone workflows from the templates
and customize them by modifying sample specification and simulation
parameters.
Output of a workflow usually includes 
the simulated scattered neutrons,
the simulated event-mode NeXus file,
and the reduced I(Q, E) file.

The MCViNE software is an open source software and is freely
available.
More details about the conditions of use and license can be found
`here <http://danse.us/trac/MCViNE/wiki/license>`_.
Feedback to the MCViNE developers can be provided through the
`MCViNE user mailing list <http://groups.google.com/group/mcvine-users>`_.



.. _features:

Features
--------

Infrastructure:

* Simple, clean command line interface for
 - Creation of simulation application (:ref:`tutorial <create-sim-app>`, :ref:`manual <fundamentals-instrument>`)
 - :ref:`Listing available neutron components <fundamentals-list-of-components>`
 - :ref:`Displaying info about any neutron component <fundamentals-component-info>`
* :ref:`Debugging facility <fundamentals-tracer>`
* :ref:`Easily extensible python/c++ interface for neutron component <extend-mcvine>`
* :ref:`Sample simulation framework <SampleAssembly>`
* Detector system simulation framework
* :ref:`Wrapping legacy packages and putting them to work in one framework <wrap-legacy-packages>`.

Generic components:

* :ref:`Neutron Printer <neutronprinter>`
* :ref:`Monochromatic Source <monochromatic source>`
* :ref:`Neutron storage (reader, writer) <neutronstorage>`
* :ref:`NDMonitor <ndmonitor>`
* :ref:`SampleAssemblyFromXml <SampleAssembly>`
* DetectorSystemFromXml

Sample scattering kernels:

* :ref:`Isotropic <kernel_isotropic>`
* :ref:`Constant energy transfer <kernel_constant-energy-transfer>`
* :ref:`Constant Q,E <kernel_constant-qe>`
* :ref:`S(Q,E) <kernel_sqe>`
* :ref:`S(Q) <kernel_sq>`
* :ref:`Simple powder diffraction (experimental) <kernel_simplepowderdiffr>`
* :ref:`Coherent inelastic phonon scattering for polycrystal <kernel_coh_inel_phonon_polyxtal>`
* :ref:`Coherent inelastic phonon scattering for single crysal <kernel_coh_inel_phonon_singlextal>`
* Detector scattering kernels:

  - He3

Instruments:

* ARCS
* VULCAN
* SEQUOIA (in progress)
* CNCS (in progress)

:ref:`McStas binding <mcstas-comp-lib>`:

* Availability of reusable mcvine-wrapped mcstas component library upon installation
* Seamless integration of mcvine-wrapped mcstas components
* (Semi-)automatic translation of mcstas component
* CLI for compiling a mcstas component to a reusable c++ shared library and a python component

Graphical user interface:

* http://vnf-dev.caltech.edu/mcvine

.. Example usages
.. --------------

.. MCViNE framework is very flexible and powerful and can take on a variety of
.. simulation problems. Here are just some simple examples:

.. 1. can simulate complex sample with scattering of various origins (phonon scattering and magnetic scattering, etc)
.. 2. can simulate accurately a real, complex detector system such as that of the ARCS instrument at SNS

