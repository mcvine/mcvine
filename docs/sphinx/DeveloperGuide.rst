Developer Guide
===============

Development environemnt
-----------------------

The following instructions work for ubuntu 14.04LTS 64bit

Basic dev tools
* make
* c++ compiler
* python
* git

Dependencies:
* boost-python, gsl
* numpy, matplotlib
* h5py
* psutil


::
 $ apt-get install git
 $ apt-get install g++
 $ apt-get install python-dev libboost-python python-numpy python-matplotlib python-h5py python-psutil
 $ apt-get install libboost-python1.55.0 libboost-python1.55-dev
 $ apt-get install libgsl0-dev

Create dev directory::

 $ cd $HOME
 $ mkdir dv
 $ cd dv

Get releaser::

 $ git clone git@githut.com:heetuu/mcvine-releaser mcvine

Get source::

 $ cd mcvine
 $ ./getsrc.py

Env vars to build::
 $ export BOOSTPYTHON_DIR=/usr
 $ export BOOSTPYTHON_LIBDIR=/usr/lib/x86_64-linux-gnu

Build::
 $ ./build.py

Env vars to use mcvine::
 $ . ~/dv/mcvine/EXPORT/bin/envs.sh

Run a test::
 $ cd ~/dv/mcvine/src/mcvine/packages/mcni/tests/mcni
 $ ./alltests.py

Build during development::
 $ . ~/dv/mcvine/src/dottools # once for one session
 $ cd /place/where/code/were/modified
 $ mm


Links
-----

* automatic build and testing (buildbot): http://bagua.cacr.caltech.edu:50082/


Creating a new scattering kernel for sample
-------------------------------------------

Write c++ class
^^^^^^^^^^^^^^^

Inherit from AbstractScatteringKernel and implement new kernel.

The following is a partial definition of an example kernel that scatters neutrons according to a S(Q,E) function supplied by user::


    /// scattering kernel of S(Q,E).
    /// S(Q,E) kernel where Q is scalar.
    class SQEkernel : public AbstractScatteringKernel {
    public:
      
      // meta methods
      //! ctor
      SQEkernel( double scattering_cross_section,
                 double density,
		 const sample::AbstractSQE & sqe, 
		 double Qmin, double Qmax,
		 double Emin, double Emax) ;
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void scatter( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      ...

    }; // class SQEkernel


Source:
 - [source:trunk/packages/mccomponents/libmccomponents/kernels/sample/SQEkernel.h Declaration]
 - [source:trunk/packages/mccomponents/libmccomponents/kernels/sample/SQEkernel.cc Definition]


Details:

 * add header file to Make.mm at the same directory
 * add cc file to Make.mm at libmccomponents/sharedlib

Create boost python binding
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To create binding of a new c++ kernel class, you will need to

 1. write the boost python binding code in a c++ source file
 1. call this new binding code in your main binding module source file
 1. update your Make file or Make.mm to include new source
 1. rebuild binding 

Boost python binding
""""""""""""""""""""

Boost python binding can be added to directory mccomponents/mccomponentsbpmodule.

The following is an example::

 // headers for the new kernel
 #include "mccomponents/kernels/sample/AbstractSQE.h"
 #include "mccomponents/kernels/sample/SQEkernel.h"
 // header for binding
 #include "mccomponents/boostpython_binding/wrap_kernel.h"
 
 namespace wrap_mccomponents {
 
   void wrap_SQEkernel()
   {
     using namespace boost::python;
     using namespace mccomponents::boostpython_binding;
     using namespace mccomponents::sample; 
 
     typedef mccomponents::kernels::SQEkernel w_t; // The class to bind
 
     kernel_wrapper<w_t>::wrap  
       ("SQEkernel",  // name of the class accessible in python
        init<double, double,  // the constructor. just copy the constructor argument types here
        const AbstractSQE &, 
        double, double, double, double> () 
        [with_custodian_and_ward<1,4> () // with_custodian_and_ward to connect life time of objects (more about this in ???)
        ]
        )
       ;
   }
 }

Please note that here that kernel_wrapper<w_t>::wrap is a shortcut
for wrapping a kernel.


Create python handlers
^^^^^^^^^^^^^^^^^^^^^^

* Binding wrapper: new method in module mccomponents.sample.bindings.BoostPythonBinding
* python class for the kernel: new module in subpackage mccomponents.sample (don't forget Make.mm)
* factory method for the kernel: new method in subpackage mccomponents.sample (__init__.py)
* handler for computation engine renderer: new method in mccomponents.sample.ComputationEngineRendererExtension
* xml handler: in subpackage mccomponents.sample.kernelxml
 - Renderer (new handler method)
 - parser.Document (new stub)
 - parser.HomogeneousScatterer (new handler method)
 - parser.KernelContainer (new handler method)
 - parser.ScateringKernel (new handler method)
 - parser.<kernel-name> (new module)
 - parser/Make.mm (new entry for the new kernel module)
* test case: new module in mccomponents/tests/sample

The steps presented here are good for more-or-less generic sample kernels.
It is desirable in many cases to group kernels into subpackages of
mccomponents.sample, for example, mccomponents.sample.phonons.


.. _wrap-legacy-packages:

Legacy Monte Carlo Neutron Scattering Simulation Packages based on pipeline structure
-------------------------------------------------------------------------------------

.. note::
   To see how to use components from legacy packages,
   please refer to :ref:`mcstas-comp-lib` and :ref:`vitess-comp-lib`.

Please read :ref:`philosophy`
to get a feeling of the architecture and design of mcvine.

MCViNE is compatible with other pipeline-based Monte Carlo
neutron scattering simulation packages.
The basic idea is to wrap legacy components in python to
be compatible with the mcvine neutron component interface.

.. _wrap-mcstas:

McStas
------
In mcstas, each component is written in c language with some extra 
paragraphs written in mcstas meta language.

To wrap a mcstas componet in mcvine, mcvine parses the component file
to extract information about the component such as name, help text,
type and default value for parameters, and code blocks for intialization,
finalization, and neutron-processing, and build a c++ class from it,
and then use boost python to bind the c++ class to python, and finally
add a python wrapper on top of the python binding.



Shapes
------

more shapes: 
sampleassembly.saxml.parser.Document



Tests
-----

Some tests may need data files. 
These data files are "MCViNE resources": https://github.com/heetuu/mcvine-resources.
The directory of the MCViNE resources should be assigned to
env var MCVINE_RESOURCES.


Python Tests
^^^^^^^^^^^^
To skip a python test from the test harness, put ::

  skip = True

near the top of the test module.

