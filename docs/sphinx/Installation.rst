.. _installation:

Installation
============

For a list of systems already deployed with MCViNE, please go to
:ref:`deployments <deployments>`.

At this moment, mcvine can only be installed from source.


Build mcvine from source
------------------------

.. note::
   `Docker <https://www.docker.com/>`_ is used to test
   installation of MCViNE on various Linux systems.
   Related Dockerfiles can be found in
   https://github.com/mcvine/releaser/tree/master/docker,
   and they can be used as hints for installing dependencies
   and then building mcvine.


To install mcvine from source, please follow these steps:

* :ref:`Obtain MCViNE source <obtain-mcvine-source>`
* :ref:`Check and install dependencies <check-deps>`
* :ref:`Run install script <run-install>`

.. _obtain-mcvine-source:

Obtain mcvine source
^^^^^^^^^^^^^^^^^^^^
You can obtain 
:ref:`mcvine source from github <install-src-git>`.

.. _install-src-git:

From github repository
""""""""""""""""""""""
Check out MCViNE by ::

 $ git clone https://github.com/mcvine/releaser mcvine

and change into the checked-out directory::

 $ cd mcvine


.. _install-src-repo-on-web:

DANSE package repository on the web
"""""""""""""""""""""""""""""""""""

You can get a source distribution of mcvine
from http://dev.danse.us/packages/mcvine-src-dist.tgz. 
You will need
to expand it somewhere::

 $ tar -xvzf mcvine-src-dist.tgz

and change into the expanded directory::

 $ cd mcvine-src-dist

.. _check-deps:

Before you install
^^^^^^^^^^^^^^^^^^
MCViNE is written in C++ and Python, and it is required
that the
following essential development tools are available 
in your system:

* make
* gcc c++ compiler
* python
* git

It also depends on some python packages:

* numpy
* h5py
* psutil

and the GNU scientific library (gsl).

Boost python is required for generating python bindings of mcvine c++ libraries.
You may need to let mcvine installer know about your boost python installation by ::

 $ export BOOSTPYTHON_DIR=/path/to/boost/python

If you want to take advantage of parallel computing, please install
mpich2. After installation of mpich2, you will need include mpich2 
executables such as mpicxx in your PATH, so that the following
command does not complain about "command not found"::

 $ mpicxx


.. _run-install:

Build and Install
^^^^^^^^^^^^^^^^^

To start, please run the build.py command::

 $ ./build.py <export_root>

Here, <export_root> is the path where you want mcvine installed.
If left empty, it will by default be the sub-directory "EXPORT"
in the current directory.

The script will see if the dependencies are installed;
if it cannot find a dependency, it will ask if
you allow it to try to install it for you.
You may decide to install the dependency yourself 
and come back here to run the script again.

If everything goes fine. You will have a mcvine installation built
under the directory you specified in the command
line, and the following command ::

 $ ls <export_root>

will output something like::

 bin  docs  etc  include  lib  modules  share

This will conclude the installation. 
To try your installation out, please do
the following::

 $ source <export_root>/bin/envs.sh
 $ mcvine-component-info -type=E_monitor

.. You should see mcvine 
.. starting to compile the mcstas E_monitor
.. component (this will happen only once for every type of 
.. mcvine-wrapped mcstas component. Built-in mcvine components
.. don't need this step) and then show some info about the E_monitor
The 2nd command will print some info about the E_monitor
component. If you see anything unexpected, there must be some
problems in the installation; please don't hesitate to post
a message to the mcvine user discussion group 
mcvine-users at googlegroups dot com.

.. note::
  The command ::
  
   $ source <export_root>/bin/envs.sh
  
  build the environment necessary for using mcvine. 
  You may want to look into it and make it part of your 
  .bashrc.


MCViNE-wrapped McStas components
""""""""""""""""""""""""""""""""
Optional: 
to set the path of the mcvine-wrapped mcstas component library, please
set the environment variable "MCSTAS_COMPONENT_LIBDIR". For example,
you can set it by::

 $ export MCSTAS_COMPONENT_LIBDIR=/path/to/mcvine/EXPORT/share/mcstas2/McStas-Components


By default, however, you don't need to set it and mcvine will try 
to find it in default locations.


.. .. _platform-specific-instructions:

.. Platform specific instructions
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. If using mpich2, need to set the following environment variables::
.. 
..  $ export MPI_DIR=/usr/lib/mpich2
..  $ export MPI_INCDIR=/usr/include/mpich2-i386
..  $ export MPI_LIBDIR=$MPI_DIR/lib
..  $ export PATH=$MPI_DIR/bin:$PATH


.. _buildnotes:

Build notes
-----------

SNS machines
^^^^^^^^^^^^
Before running "./build.py", 
please let mcvine know about the mpich2 installation::

 $ export MPI_DIR=/usr
 $ export MPI_INCDIR=/usr/include/mpich2-x86_64
 $ export MPI_LIBDIR=/usr/lib64/mpich2/lib

Now you can run build.py::

 $ ./build.py

It will ask if you want to install h5py and boostpython, please
answer with yes.



.. _deployments:

Deployments
-----------

DANSE clusters at Caltech CACR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

foxtrot.danse.us
""""""""""""""""
MCViNE is available through the "modules" package manager.

To use mcvine, run ::

 $ module add python wx h5py mcvine



ARCS clusters at SNS
^^^^^^^^^^^^^^^^^^^^
MCViNE is tentatively installed on arcs clusters at SNS. 
You can use it at arcs1 and arcs2 clusters.

To use mcvine, run ::

 $ source ~linjiao/mcvine.sh


Systems tested
--------------

* Ubuntu 
 - 14.04

* Fedora
 - 21

* Cent OS
 - 6
