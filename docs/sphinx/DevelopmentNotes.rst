.. _devnotes:

Development notes
=================

Workflow
--------

* Code: http://github.com/mcvine/workflow
* CLI: $ mcvine workflow
* CLI impl.: https://github.com/mcvine/workflow/tree/master/mcvine_workflow/cli
* Workflow examples:
  - https://github.com/mcvine/workflow/tree/master/notebook-examples
  - https://github.com/mcvine/training/: subdirs such as ARCS


Instrument Simulation App
-------------------------
An instrument simulation app is a pyre application.
Its inventory contains 

* neutron_components: a list of component names
* each neutron component as a pyre component

The run method of the app first prepare the simulation context,
then run a loop that send neutrons through the simulation compoonent 
list.

The run_postprocessing method of the app can be called to 
run the postprocessing scripts written out by monitor-like
components (`here <https://github.com/mcvine/mcvine/blob/7cd386bbf545c7bbe8d0259340ac8fa247bfa88d/packages/mcni/python/mcni/pyre_components/NeutronToStorage.py#L67>`_ is an example).

It is better that the run_postprocessing method be called in a different
process than the process that executes the "run" method.
This is achieved in `InstrumentBuilder <https://github.com/mcvine/mcvine/blob/7cd386bbf545c7bbe8d0259340ac8fa247bfa88d/packages/mcvine/python/mcvine/applications/InstrumentBuilder.py#L27>`_.


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

* convert mcstas instrument to python scripts
  - modify mcstas instrument file
    - convert to unix format ("\r\n"->"\n") using dos2unix
    - make sure that in the "DEFINE INSTRUMENT" line all parameters have default values
    - if c code snippets exist in the "DECLARE" or "INITIALIZE", move all of them
      to "INITIALIZE" section (python vars don't need declaration),
      and make sure the to convert them into python syntax
    - clean up the component definitions so that the "AT ..." clause
      and "ROTATED ..." clause are in two different lines.
      Also add a space between "AT/ROTATED" and "(...)" if there is none.
  - $ mcvine mcstas convertinstrument <instrument-file>
    This cmd generates
    - "config-SIM" script: use this to generate configuration of the instrument simulation
    - "SIM" script: run this script to simulate
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


Command line interface
----------------------

The main command::

 $ mcvine

It is implemented using python-click: http://click.pocoo.org/.
The main command is at /packages/mcvine/python/mcvine/cli.
sub-cmds are imported from various sub-packages such as mcstas2 
and mcvine.instruments.


Provenance
""""""""""
is achieved using "save_metadata" decorator.
See mcvine.cli._provenance for implementation details.

pyre commands
"""""""""""""
Pyre applications are built using pyre machineries and they
have configurable components.

Pyre super applications are pyre app wrappers and is made in mcvine.
The design of pyre-super-app is not optimal but it serves
the purpose of simplification of command line interface
for some applications with a lot of components and 
parameters to set.


Resources
---------

Organization:
* instruments: 
  - each directory corresponds to one instrument
  - subdirs of an instrument
    - moderator
    - detsys
    - nxs
    - simulations
* samples:
  - any directory with sampleassembly.xml is a sample assembly folder
  - other directories could provide various kinds of data
  - hierarchy: matter/temperature/shape/...  For example: V/300K/plate


McStas component library: its path is set by env var $MCSTAS_COMPONENT_LIBDIR.


Logging
-------

* Use both pyre journal and python logging
* pyre journal configured by pml files
* logging configured by "mcvine.conf" (see mcvine toplevel __init__.py)
  - example: tests/logger/mcvine.conf


Documentation
-------------

* github:mcvine/mcvine.org
  mcvine.org site
* github:mcvine/mcvine.github.io:master
  Documentation for all releases
* github:mcvine/mcvine:gh-pages
  Documentation for the development version


