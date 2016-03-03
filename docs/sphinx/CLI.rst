.. _cli:

Command line interface
======================

mcvine
------

The main command line interface (CLI) of the MCViNE package is the command "mcvine".
Execute::

 $ mcvine

will list available subcommands.


bash
----

If you are using bash, you can use the following command to add bash auto-complete
support::

 $ eval "$(_MCVINE_COMPLETE=source mcvine)"

You can also establish aliases to some long commands. For example::

 $ eval `mcvine bash aliases arcs`

will create aliases for commands related to the ARCS spectrometer, which 
include a series of aliases starting with prefix "arcs". For example,
"arcs_beam" is an alias of "mcvine instruments arcs beam".


instruments
-----------

Subcommands for neutron instruments. For example::

 $ mcvine instruments arcs

provide commands for the ARCS spectrometer at SNS


phonon
------

Command::

 $ mcvine phonon

Phonon-related functionalities.

Given phonon data in IDF format, it can

* extract band structure
* compute neutron scattering data slice


Misc
----

mcstas support::

 $ mcvine mcstas compilecomponent --filename=<path-to-component> --category=<component-category>


Check sample assembly xml::

 $ mcvine sampleassembly check <xmlpath>



