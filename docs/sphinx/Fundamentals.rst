.. _Fundamentals:

Fundamentals
============


.. _fundamentals-instrument:

Instrument
----------

Creat instrument simulation applicatioin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   You may want to follow 
   :ref:`this tutorial <create-sim-app>`.

.. note::
   Experimental: you could also create your simulation application online at
   http://vnf-dev.caltech.edu/mcvine


Create an instrument simulation application::

  $ mcvine-create-instrument-simulation-application  --name=<name> --components=<list of components>



.. _fundamentals-instrument-positioning-of-components:

Positioning of Components
^^^^^^^^^^^^^^^^^^^^^^^^^
Positioning of components is done through the "geometer"::

 --geometer.<component>=<position>,<orientation>

E.g.::

 --geometer.sample=(0,0,10),(0,0,0)

The first tuple (0,0,10) means the position of the sample is at (0,0,10).
The second tuple (0,0,0) menas the orientation of the sample is the same
as the absolute coordinate system.

.. note::
   Coordinate system convention: 

   mcvine uses the same convention as mcstas.
   
   * z -- beam downstream
   * y -- vertical up.


.. note::
   Units: 
   
   * position: meters
   * orientation: degrees


Relative coordinates
""""""""""""""""""""
A coomponent's position and orientation can be specified as relative to another
component. For example ::
   
 --geometer.sample=relative("source",(0,0,10)),relative("source",(0,30,0))

means the sample is at (0,0,10) relative to the coordinate system attached to 
the "source" component, and rotated 30 degrees by the y axis of the coordinate
system attached to the "source" component.

The reference component is specified by its name.

You can also use the keyword "previous" to mean the reference
component is the one just before this component in the pipeline.



Options of instrument simulation app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scattering
""""""""""

* --multiple-scattering: indicates whether multiple scattering is on. This option
  is only useful for the components that support this feature.

Monte Carlo
"""""""""""

* --ncount=<n>: number of simulation runs
* --buffer_size=<n>: (optional) number of neutrons buffered in memory. By default a value will be picked for you depending on ncount and memory size.


Outputs
"""""""
* --overwrite-datafiles:
  If on, existing outputs will be overwritten.
* --output-dir=<dir>:
  The output directory.

Miscellanesous
""""""""""""""

* --journal.info.instrument: as simulation progress, print out information
  regarding simulation loops and component processing loops.
* --dump-pml:
  Writes out pml file for the simulation. A pml file is a configuration file
  that contains all configuration details of the simulation application.
  When this option is on, no real simulation will be done.
* --tracer:
  facility to trace neutrons. By default, no tracer will be used. Choices:

  * --tracer=console: print out neutrons to console. Be sure to turn down ncount.

* --mpirun.nodes=<n>:
  Select the number of nodes to parallely run the simulation.
  <n> is an integer.
  This option is only valid if mpi binding of mcvine is available.


.. _fundamentals-tracer:

Using tracer to debug
---------------------
To see how neutrons move through the components,
use the "tracer" facility. 

For example, if your simulation application is named "myapp", please
try the following::

 $ /path/to/myapp --tracer=console --ncount=10

The simulation will print out the neutrons before they enter each 
component and after they exit each component.


.. _fundamentals-simulated-intensities:

Simulated intensities
---------------------
The simulated intensities at monitors are normalized by "ncount",
the number of Monte Carlo runs.


.. _fundamentals-list-of-components:

List of available neutron components
------------------------------------
To list all components::

 $ mcvine-list-components

To list components of a specific category::

 $ mcvine-list-components --category=monitors


.. _fundamentals-component-info:

Show component information
--------------------------

To find out more information about a component, run ::

 $ mcvine-component-info --type=<component-type>

For example::

 $ mcvine-component-info --type=E_monitor



Error bar of simulated intensities
----------------------------------

.. _fundamentals-errorbar-basic:

Basic treatment
^^^^^^^^^^^^^^^

Here we examine the variance, or :math:`\sigma^2` of the simulated
intensities at virtual monitors.


Let us think of a bin in a histogram gathered in a virtual monitor.
Say, in a virtual experiment that bin get the total intensity, 
:math:`I`, 

.. math::
   I = \sum p_i

where :math:`p_i` is the probability of each neutron event recorded
in the target bin.
Our purpose here is to find the variance of the intensity :math:`I`,
:math:`Var(I)`, or :math:`\sigma^2_I`.

First, let us think about this problem intuitively.
Apparantly with more events fall in to the target bin,
we expect the variance will reduce with respect to 
the total intensity :math:`I`. A good approximation would be that
the relative error, :math:`\frac{\sigma_I}{I}`, will reduce
in the order of :math:`\sqrt{N}`, where :math:`N` is the
total number of events fall in the bin.

Now, let us try to do a quantitative treatment of this problem.
To start, let us not worry about the fact that the number
of events, :math:`N`, is a result of random process. Let us assume
that :math:`N` is a fixed number, and try to find out :math:`Var(I)`:

.. math::
   Var_1(I) &= Var(\sum p_i)	\\
   	  &= \sum Var(p_i)	\\
	  &= N Var(\bar{p})

where :math:`\bar{p}` is the mean value of the collection
:math:`\{p_i\}`, or :math:`\bar{p}=\frac{1}{N}\sum{p_i}`.

The variance of :math:`\bar{p}` can be estimated by

.. math::
   Var(\bar{p}) &= \frac{1}{N-1} \sum{(p_i-\bar{p})^2} \\
   		&= \frac{1}{N-1} (\sum p^2_i - \frac{1}{N} {(\sum p_i)}^2) \\
   		&= \frac{1}{N-1} (\sum p^2_i - N \bar{p}^2)

and 

.. math::
   Var_1(I) = \frac{N}{N-1} (\sum p^2_i - N \bar{p}^2)

Now, let us think about the effect of number of events being random.
The variance resulted from that can be estimated as

.. math::
   Var_2(I) &= Var(N) \times \bar{p}^2 \\
   	    &= N \times \bar{p}^2

So we have

.. math::
   Var(I) &= Var_1(I) + Var_2(I) \\
   	  &= \frac{N}{N-1} (\sum{p_i^2} - \bar{p}^2)

In most cases, this could be approximated as

.. math::
   Var(I) = \sum{p_i^2}

To see if this is a reasonable estimate, let us consider a special case 
in which most of :math:`p_i` have similar value. In that case,

.. math::
   Var(I) &= \sum{\bar{p}^2} \\
   	  &= N\bar{p}^2 = I^2/N

or

.. math::
   \frac{\sigma_I}{I} &= \frac{\sqrt{Var(I)}}{I} \\
   		      &= \frac{1}{\sqrt{N}}

which is consistent with our intuitive guess.

The error bar of the intensity is then

.. math::
   Err(I) = \sqrt{Var(I)} = \sqrt{\sum{p_i^2}}

or 

.. math::
   Err^2(I) = \sum{p_i^2}


.. _fundamentals-errorbar-errorprop:

Error propagation
^^^^^^^^^^^^^^^^^

In the above discussion we assumed that the probablities
:math:`{p_i}` are computed precisely and have no errors
themselves. 
But there are cases that :math:`{p_i}` itself has intrinsic errors.

In some cases, the intrinsic relative error can be seen as constant
among all computed events:

.. math::
   \frac{Err_{intrinsic}(p_i)}{p_i} = \Delta_{intrinsic}

And the intensity, I, has therefore the same intrinsic relative error:

.. math::
   \frac{Err_{intrinsic}(I)}{I} = \Delta_{intrinsic}

The total relative error considering the intrinsic error
and the error discussed above in :ref:`fundamentals-errorbar-basic`, is then

.. math::
   {[\frac{Err(I)}{I}]}^2 &= \frac{Var(I)}{I^2} + \Delta_{intrinsic}^2 \\
   			  &= \frac{\sum{p_i^2}}{I^2} + \Delta_{intrinsic}^2

or

.. math::
   Err^2(I) = \Delta_{intrinsic}^2 \times I^2  + \sum{p_i^2}
