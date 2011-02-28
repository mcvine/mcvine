Tutorials -- basics
===================


Quick simulation: "mcvine-simulate"
-----------------------------------

.. note::
   This is the "quick" way of simulating neutron experiments with mcvine if you 
   are impatient and want to see some results from mcvine quickly. 
   A better approach to run your mcvine simulation is presented in :ref:`create-sim-app`.

By going through this tutorial you can get a feeling of the structure 
of mcvine component chain and utilities about
available neutron component types.

The command we introduce here is "mcvine-simulate".

To start, just use option "-h" to see a brief help message::

 $ mcvine-simulate -h

Instrument consists of a list of components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To simulate an instrument consisting of two components source, and monitor, we
start building our simulation command by ::

 $ mcvine-simulate --components=source,monitor ---

At the end of the command, "---" is a separator. After this separator, you will
provide more details of those components.

Types of components
^^^^^^^^^^^^^^^^^^^
Now, we need to specify what each of these components are.
We set the source component to a monochromatic source by ::

 --source=MonochromaticSource

And similarly, we can set the monitor ::

 --monitor=E_monitor

To find out what are the component types you can use, run ::

 $ mcvine-list-components

You can also tell the command to list components in specific category. For example ::

 $ mcvine-list-components --category=monitors

To find out more information about a specific component you are interested in, for example
the E_monitor component, run ::

 $ mcvine-component-info --type=E_monitor


Positions of components
^^^^^^^^^^^^^^^^^^^^^^^
Now, you could specify the position and orientation of a component by referring to "geometer" ::

 --geometer.monitor=[0,0,1],[0,0,0]

The syntax is actually ::

 --geometer.monitor=<position>,<orientation>

Position is a 3-vector, and the unit is meter.
Orientation is a 3-vector that denotes three consecutive rotations along
x, y, and z axes. 
The unit is degrees.


Configurations of components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Each component has several parameters that define the scattering properties of the
component. To find out the parameters for a component, use the command 
"mcvine-component-info" ::

 $ mcvine-component-info --type=E_monitor

The output would be ::

  ======================================================================
  E_monitor: Energy-sensitive monitor.
  ----------------------------------------------------------------------
  A square single monitor that measures the energy of the incoming neutrons.
  
   Example: E_monitor(name, xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1, Emin=1, Emax=50, nchan=20, filename="Output.nrj")

   
  ----------------------------------------------------------------------
  Parameters:
    * Emin: Minimum energy to detect (meV) 
    * Emax: Maximum energy to detect (meV) 
    * filename: Name of file in which to store the detector image (text) 
    * nchan: Number of energy channels (1) 
    * xmax: Upper x bound of detector opening (m) 
    * xmin: Lower x bound of detector opening (m) 
    * ymin: Lower y bound of detector opening (m) 
    * ymax: Upper y bound of detector opening (m) 
  ======================================================================


If you want to change parameter "nchan", you need ::

 --monitor.nchan=10

To sum it up, you could construct a simulation command ::
  
  $ mcvine-simulate --components=source,monitor --- \
        --source=MonochromaticSource --monitor=E_monitor \
	--geometer.source=[0,0,0],[0,0,0] --geometer.monitor=[0,0,1],[0,0,0] \
	--source.energy=60 \
	--monitor.Emin=50 --monitor.Emax=70 --monitor.nchan=100 --monitor.filename=IE.dat 
  
When this command is run, an output file "IE.dat" will be created.
This output file is in mcstas format, because the monitor "E_monitor" is 
from mcstas.
But there are other output files generated as well from this monitor
by mcvine, which are histogram hdf5 files.
You can run command ::

  $ PlotHist.py out/IE.h5

to see the output histogram.

.. image:: /screenshots/I(E).png
   :width: 400



.. _create-sim-app:

Create your own simulation application: mcvine-create-instrument-simulation-application
---------------------------------------------------------------------------------------
To create a mcvine simulation application named "test" with two components, source and monitor,
do ::

  $ mcvine-create-instrument-simulation-application  --name=test --components=source,monitor

A python application will be created and named "test".

You can find out how to run this simulation application by ::

  $ ./test -h

which outputs::

  ------------------------------------------------------------
  * Instrument simulation application 'test'
  ------------------------------------------------------------
  * Sequence of components:
     [source] --> [monitor]
  ------------------------------------------------------------
  * Command:
   $ test  \
    --dumpconfiguration=<If set, dump configuration to a pml file> \
    --multiple-scattering=<if true, enable multiple scattering> \
    --dumpconfiguration-output=<dumpconfiguration-output> \
    --buffer_size=<size of neutron buffer. This is for optimizing the preformance of the simulation. When it is too large, it will occupy too much memory. When it is too small, the simulation will be slow. If you are not sure, please just leave it unset so that the default value will be used.> \
    --output-dir=<output directory> \
    --ncount=<number of total neutrons generated by source> \
    --overwrite-datafiles=<overwrite data files?> \
    --geometer.source=<position>,<orientation> \
    --geometer.monitor=<position>,<orientation> \
    --source=<component type> \
    --monitor=<component type>
  ------------------------------------------------------------

Now, you can run this instrument by specifying more details of the instrument.
For example::

  $ ./test --source=MonochromaticSource --monitor=E_monitor

will run a simulation of an instrument with two components:

* source: MonochromaticSource
* monitor: E_monitor

You can save your configuration of the simulation application to a file so that 
it is easier to rerun it. For example::

  $ ./test --source=MonochromaticSource --monitor=E_monitor --dump-pml

will create a file "test.pml" in the current working directory.
It is a xml file and it is quite easy to understand.

Note, if you run --dump-pml again, 
the old "test.pml" will be copied to a file named like "test.pml.saved-<time>",
and the "test.pml" will be overwritten.

With this configuration file at the current working directory, you don't
need to specify the same configuration again. For example, this command ::

  $ ./test -h

now gives the following help message because it has the 
information from the test.pml file about which types of neutron components are used::

  ------------------------------------------------------------
  * Instrument simulation application 'test'
  ------------------------------------------------------------
  * Sequence of components:
     [source] --> [monitor]
  ------------------------------------------------------------
  * Command:
   $ test  \
    --multiple-scattering=<if true, enable multiple scattering> \
    --buffer_size=<size of neutron buffer. This is for optimizing the preformance of the simulation. When it is too large, it will occupy too much memory. When it is too small, the simulation will be slow. If you are not sure, please just leave it unset so that the default value will be used.> \
    --output-dir=<output directory> \
    --ncount=<number of total neutrons generated by source> \
    --overwrite-datafiles=<overwrite data files?> \
    --geometer.source=<position>,<orientation> \
    --geometer.monitor=<position>,<orientation> \
    --source=<component type> \
    --monitor=<component type> \
    --source.probability=<probabliity of neutrons. unit: 1> \
    --source.position=<position of neutrons. unit: m> \
    --source.energy=<energy of the neutron. if "energy" is given, the neutron velocity will be computed so that the energy of the neutron will be the given value of energy,and the moving direction will be determined by the "velocity" vector> \
    --source.time=<time of flight for neutrons. unit: s> \
    --source.velocity=<velocity of neutrons. unit: m/s. Note: if energy is nonzero, the magnitude of the velocity is set by energy> \
    --monitor.Emin=<Minimum energy to detect (meV) > \
    --monitor.Emax=<Maximum energy to detect (meV) > \
    --monitor.filename=<Name of file in which to store the detector image (text) > \
    --monitor.nchan=<Number of energy channels (1) > \
    --monitor.xmax=<Upper x bound of detector opening (m) > \
    --monitor.xmin=<Lower x bound of detector opening (m) > \
    --monitor.ymin=<Lower y bound of detector opening (m) > \
    --monitor.ymax=<Upper y bound of detector opening (m) >
  ------------------------------------------------------------

Further you can specify more details of your simulation and run the simualation ::

  $ ./test --source.energy=60 --monitor.Emin=50 --monitor.Emax=70 --monitor.nchan=100

or you can save the new configuration to a configuration file for future usage::

  $ ./test --source.energy=60 --monitor.Emin=50 --monitor.Emax=70 --monitor.nchan=100 \
      --dump-pml


