.. _tutorials:

Tutorials
=========


Quick simulation: "mcvine-simulate"
-----------------------------------

An easy way to run a Monte Carlo simulation of a neutron experiment
is to use the command "mcvine-simulate".

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

