Introduction
==============

To put it simple, MCViNE is a Monte Carlo simulation framework 
useful for simulating neutron experiments. 

1. MCViNE is a framework to construct simulated neutron instruments, and manage the flow of neutrons through them from moderator to detector.
2. It also provides a mechanism to allow users to assemble a complex sample component (including sample and also the sample environment, eg. sample holder). This mechanism is extensible to handle arbitrary complex geometeric shapes of neutron scatterer, and arbitrary complex physics of neutron scattering.

A natural question to ask is, how is it different from existing legacy Monte Carlo
neutron scattering code such as mcstas, vitess, etc?
Please take a moment to read :ref:`philosophy of MCViNE <philosophy>`.


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
* :ref:`powder diffraction (experimental) <kernel_powderdiffr>`
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


Example usages
--------------

MCViNE framework is very flexible and powerful and can take on a variety of
simulation problems. Here are just some simple examples:

1. can simulate complex sample with scattering of various origins (phonon scattering and magnetic scattering, etc)
2. can simulate accurately a real, complex detector system such as that of the ARCS instrument at SNS

