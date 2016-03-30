.. _tutorials-arcs:

Simulation of ARCS experiments
==============================

.. note::
   :ref:`Tricks for $ mcvine command line bash interface" <cli/bash>` may be useful
   if you need to customize the simulations in the following tutorials.



Tutorial: full simulation of an experiment of a polycrystalline Vanadium sample
-------------------------------------------------------------------------------

This is a tutorial of a full simulation of an ARCS experiment 
with a polycrystalline vanadium sample.

Following are four essential steps for such a simulation:

* Simulate the neutron beam at the sample position
* Send neutrons in the simulated neutron beam to the sample to be scattered, and save the scattered neutrons
* Send the scattered neutrons to the ARCS detector system, which generates "event-mode" nexus data
* Reduce "event-mode" nexus data to I(Q,E)


MCViNE has made these steps easier by providing some convenient tools,
so that you can run the last three steps above using only one command.
All you need to do is

#. :ref:`Create the workflow <tutorial-arcs-powderV-create-workflow>`
#. :ref:`Run the beam simulation <tutorial-arcs-powderV-beam>`
#. :ref:`Run the sample scattering, neutron detection, and reduction using one make command <tutorial-arcs-powderV-sample>`


.. _tutorial-arcs-powderV-create-workflow:

1. Create workflow
""""""""""""""""""
Run ::

   $ mcvine workflow powder --instrument=ARCS --sample=V --workdir=mysim

And a new directory "mysim" will be created. Change to this new directory::

  $ cd mysim


.. _tutorial-arcs-powderV-beam:

2. Incident beam at sample
""""""""""""""""""""""""""

In this step we simulate the ARCS instrument from moderator
down to the sample position::

  $ cd beam
  $ ./run-beam.sh

This command will run the beam simulation and when finished, generate
output files in mysim/beam/out directory.

You may want to inspect and modify "run-beam.sh" to change
some parameters.
For example, number of neutrons to simulate can be changed using
option --ncount.

.. note::
   More details of beam simulation can be found in 
   :ref:`a different tutorial below <tut_arcs_beam>`

After this step is finished, we may optionally examine the output files
(see the note below),
and then move back to the workflow directory::

  $ cd ..

..
 * Output: out/neutrons
   
   See how many neutrons are there::

     $ mcvine-neutron-storage-count-neutrons out/neutrons

.. note::
 Following are some output files

 * Output: out/mon1-itof-focused.h5 -- focused monitor 1 histogram

   To plot, execute::

     $ plothist out/mon1-tof-focused.h5

 * Output: out/mon2-itof-focused.h5 -- focused monitor 2 histogram


.. _tutorial-arcs-powderV-sample:

3. Sample scattering, neutron detection, and reduction
""""""""""""""""""""""""""""""""""""""""""""""""""""""

These three steps are combined together by the Makefile in this workflow
directory. All you need to do is to execute::

 $ make

It will run the three steps sequentially.
Each step will generate a log file. For example, the scattering step
will generate a log file "log.scatter".
They may be useful in debugging the simulation.
If any of the steps failed, the workflow will stop.

Inputs
......

The main input for the sample scattering step is the "sampleassembly"
directory, which is explained :ref:`here <SampleAssembly>`.

You may adjust the sample scattering simulation options in
the script "scatter":

* --ncount: number of neutrons
* --mpirun.nodes: number of nodes to use for parallel simulation
* --multiple-scattering: turn multiple scattering on or off

You may adjust the neutron detection simulation options in
the script "create-nxs":

* --nodes: number of nodes to use for parallel simulation

You may adjust the reduction options in
the script "reduce2iqe":

* --qaxis: Q axis specification (min, max, step)


Outputs
.......

The main output of this simulation is the I(Q,E) histogram, iqe.h5.
To plot the result::

 $ make plot-iqe



..
   Create a working directory::

     $ mkdir -p arcs-polyV
     $ cd arcs-polyV

   Let us suppose that the environment variable "workdir" is set to this new
   directory.

   1. Incident beam at sample
   """"""""""""""""""""""""""
   In this step we simulate the ARCS instrument from moderator
   down to the sample position.

   Create a directory ::

    $ mkdir mod2sample
    $ cd mod2sample

   Suppose

   * the incident energy to simulate is 100 meV
   * fermi chopper "100-1.5-SMI" is chosen
   * fermi chopper frequency is set to 600 Hz
   * T0 chopper frequency is set to 120 Hz
   * neutron count is 1e8

   We can run the arcs beam simulation (from moderator to sample)

    $ arcs_beam -E=100 -T0_nu=120 -fermi_chopper=100-1.5-SMI -fermi_nu=600 --ncount=1e8



   Scattering of incident neutrons by sample
   """""""""""""""""""""""""""""""""""""""""
   Create a directory for this::

    $ mkdir -p $workdir/scattering
    $ cd $workdir/scattering

   Create a script for this simulation::

    $ mcvine-create-instrument-simulation-application -name=ssd -components=source,sample,detector 

   Configure the script to use the correct components and save the configuration::

    $ ./ssd -source=NeutronFromStorage -sample=SampleAssemblyFromXml -detector=NeutronToStorage -h -dump-pml=yes

   Change the configuration by editing the file ssd.pml::

     <inventory>

       <component name="ssd">
	   <property name="sequence">['source', 'sample', 'detector']</property>
	   <facility name="source">sources/NeutronFromStorage</facility>
	   <facility name="sample">samples/SampleAssemblyFromXml</facility>
	   <facility name="detector">monitors/NeutronToStorage</facility>

	   <property name="multiple-scattering">False</property>

	   <property name="ncount">1e7</property>
	   <property name="buffer_size">1000000</property>

	   <property name="overwrite-datafiles">True</property>
	   <property name="output-dir">out</property>

	   <component name="sample">
	       <property name="xml">V/sampleassembly.xml</property>
	   </component>


	   <component name="source">
	       <property name="path">../mod2sample/out/neutrons</property>
	   </component>


	   <component name="detector">
	       <property name="path">neutrons</property>
	       <property name="append">False</property>
	   </component>


	   <component name="geometer">
	       <property name="source">((0, 0, 13.45), (0, 0, 0))</property>
	       <property name="sample">((0, 0, 13.6), (0, 0, 0))</property>
	       <property name="detector">((0, 0, 13.6), (0, 0, 0))</property>
	   </component>

       </component>

     </inventory>


   Create sample assembly xml file ::

     $ mkdir V
     $ cd V

   So we are now inside directory $workdir/scattering/V.
   We need to create three files in this directory:

   1. sampleassembly.xml -- the main file describes the whole sample assembly. It only contains one scatterer, V powder sample, in this case
   2. V.xyz -- xyz file describing the crystal structure of V, the material
   3. V-scatterer.xml  -- The file describing the kernels of the scatterer, the V sample.

   Here are the contents of these files:

   sampleassembly.xml::

    <SampleAssembly name="bcc V powder sample assembly">

     <PowderSample name="V" type="sample">
       <Shape>
	 <block width="100*mm" height="100*mm" thickness="2*mm" />
       </Shape>
       <Phase type="crystal">
	 <ChemicalFormula>V</ChemicalFormula>
	 <xyzfile>V.xyz</xyzfile>
       </Phase>
     </PowderSample>

     <LocalGeometer registry-coordinate-system="InstrumentScientist">
       <Register name="V" position="(0,0,0)" orientation="(0,0,45)"/>
     </LocalGeometer>

    </SampleAssembly>


   V.xyz::

    2
    3.02 0 0   0 3.02 0   0 0 3.02
    V 0  0  0
    V 0.5 0.5 0.5

   V-scatterer.xml::

    <?xml version="1.0"?>

    <!DOCTYPE scatterer>

    <!-- mcweights: monte-carlo weights for 3 possible processes: 
    absorption, scattering, transmission -->
    <homogeneous_scatterer mcweights="0, 1, 0">

     <IsotropicKernel>
     </IsotropicKernel>

    </homogeneous_scatterer>

   Run the simulation::

     $ ./ssd

   Output: out/neutrons
   See how many neutrons are there::

    $ mcvine-neutron-storage-count-neutrons out/neutrons


   (Optional) check the I(Q,E) using an ideal I(Q,E) monitor::

    $ checksqe -source.path=out/neutrons -monitor.Ei=100 -monitor.Emin=-95 -monitor.Emax=95 -monitor.nE=190 -monitor.Qmin=0 -monitor.Qmax=13 -monitor.nQ=130


..
   Tutorial 2: Compute resolution function in Q,E space
   ----------------------------------------------------

   See :ref:`Command "arcs-compute-IQE-resolution" <arcs-iqeres>`


   Commands
   --------

   .. _arcs_beam:

   arcs_beam
   """""""""

   Compute neutrons at the sample position of ARCS beam.
   The neutrons computed will be saved in a file, which
   can be reused to simulate sample scattering.
   So make sure to keep those neutron files somewhere,
   and usually you don't want to delete them.

   Run ::

    $ arcs_beam -h

   to find help

   .. _arcs-iqeres:

   arcs-compute-IQE-resolution
   """""""""""""""""""""""""""

   Compute I(Q,E) resolution function.

   To run this simulation, you will need to compute neutrons at
   sample position for ARCS. This can be done by running
   the :ref:`arcs_beam <arcs_beam>` command.


   Example command::

    $ arcs-compute-IQE-resolution --ncount=1e7 --nodes=10 --Ei=100 --Q=6  --E=20 --dQ=2 --dE=10 --mod2sample=/path/to/mod2sample

   * ncount: Monte Carlo counts
   * nodes: number of nodes
   * Ei: nominal incident energy (meV)
   * Q, E: momentum and energy transfer at which the resolution is calculated
   * dQ, dE: range of momentum and energy transfer in which the resolution function is computed
   * mod2sample: the path in which the moderator-to-sample simulation was performed.



   arcs-neutrons2nxs
   """""""""""""""""

   Convert scattered neutrons into nexus data file.

   ::

    $ arcs-neutrons2nxs --neutrons=<neutron-file> --nxs=<nexus-output-file> --workdir=<temporary-working-dir>

   * neutrons: input neutron file. This file must be generated from a mcvine simulation of 
     sample-scattered neutrons
   * nxs: output nexus data file. default: arcs-sim.nxs
   * workdir: temporary working dir. default: work


.. _tut_arcs_beam:

Tutorial: Simulation of ARCS beam
---------------------------------


Here we simulate the ARCS instrument from moderator
down to the sample position.

Create a directory ::

 $ mkdir mod2sample
 $ cd mod2sample

Suppose

* the incident energy to simulate is 100 meV
* fermi chopper "100-1.5-SMI" is chosen
* fermi chopper frequency is set to 600 Hz
* T0 chopper frequency is set to 120 Hz
* neutron count is 1e8

We can run the arcs beam simulation (from moderator to sample)

 $ arcs_beam -E=100 -T0_nu=120 -fermi_chopper=100-1.5-SMI -fermi_nu=600 --ncount=1e8

Output: out/neutrons

.. See how many neutrons are there::
   $ mcvine-neutron-storage-count-neutrons out/neutrons

Output: out/mon1-itof-focused.h5

.. Plot::
   $ plothist out/mon1-tof.h5

Output: out/mon2-itof-focused.h5

.. Plot::
   $ plothist out/mon2-tof.h5


.. _arcscmds:

Command line interface for ARCS
-------------------------------

To find out available simulation applications for the ARCS spectrometer::

 $ mcvine instruments arcs

To use bash aliases for ARCS related commands::

 $ eval `mcvine bash aliases arcs`
