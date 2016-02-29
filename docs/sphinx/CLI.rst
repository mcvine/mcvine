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

You can also establish some aliases to some long commands. For example::

 $ eval `mcvine bash aliases arcs`

will create aliases for commands related to the ARCS spectrometer, which 
include a series of aliases starting with prefix "arcs". For example,
"arcs_beam" is an alias of "mcvine instruments arcs beam".


Misc
----

mcstas support::

 $ mcvine mcstas compilecomponent --filename=<path-to-component> --category=<component-category>


Check sample assembly xml::

 $ mcvine sampleassembly check <xmlpath>



