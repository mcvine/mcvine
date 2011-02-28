Introduction
==============

To put it simple, MCViNE is a Monte Carlo simulation framework 
useful for simulating neutron experiments. 

1. MCViNE is a framework to construct simulated neutron instruments, and manage the flow of neutrons through them from moderator to detector.
2. It also provides a mechanism to allow users to assemble a complex sample component (including sample and also the sample environment, eg. sample holder). This mechanism is extensible to handle arbitrary complex geometeric shapes of neutron scatterer, and arbitrary complex physics of neutron scattering.

A natural question to ask is, how is it different from existing legacy Monte Carlo
neutron scattering code such as mcstas, vitess, etc?
Please take a moment to read :ref:`philosophy of MCViNE <philosophy>`.


Features
--------

Infrastructure:

* Simple, clean command line interface for
 - Creation of simulation application (:ref:`tutorial <create-sim-app>`, :ref:`manual <fundamentals-instrument>`)
 - :ref:`Listing available neutron components <fundamentals-list-of-components>`
 - :ref:`Displaying info about any neutron component <fundamentals-component-info>`
* :ref:`Debugging facility <fundamentals-tracer>`
* :ref:`Easily extensible python/c++ interface for neutron component <extend-mcvine>`
* Sample simulation framework
* Detector system simulation framework
* XML schema for sample assembly configuration
* Wrapping legacy packages and putting them to work in one framework

Generic components:

* Neutron Printer
* Monochromatic Source
* Neutron storage (reader, writer)
* NDMonitor
* SampleAssemblyFromXml

Sample scattering kernels:

* Isotropic
* Constant energy transfer
* Constant Q,E
* S(Q,E)
* S(Q)
* powder diffraction (experimental)
* Coherent inelastic phonon scattering for polycrystal
* Coherent inelastic phonon scattering for single crysal
* Detector scattering kernels:
  - He3

Instruments:

* ARCS
* VULCAN
* SEQUOIA (in progress)
* CNCS (in progress)

McStas binding:

* Seamless integration of mcvine-wrapped mcstas components
* (Semi-)automatic translation of mcstas component
* Availability of reusable mcvine-wrapped mcstas component library upon installation
* CLI for compiling a mcstas component to a reusable c++ shared library and a python component


Example usages
--------------

MCViNE framework is very flexible and powerful and can take on a variety of
simulation problems. Here are just some simple examples:

1. can simulate complex sample with scattering of various origins (phonon scattering and magnetic scattering, etc)
2. can simulate accurately a real, complex detector system such as that of the ARCS instrument at SNS

