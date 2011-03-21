.. _installation:

Installation
============

For a list of systems already deployed with MCViNE, please go to
:ref:`deployments <deployments>`.

At this moment, mcvine can only be installed from source.

Build mcvine from source
------------------------

.. note::
  You may want to read :ref:`platform specific instructions <platform-specific-instructions>`
  first before you move on.


Obtain mcvine source
^^^^^^^^^^^^^^^^^^^^
To obtain mcvine source, you can either get it from
:ref:`danse svn repository <install-src-svn>`
or 
:ref:`danse web site <install-src-repo-on-web>`.


.. _install-src-svn:

Subversion repository
"""""""""""""""""""""
If subversion is available in your system and anonymous svn checkout
is not blocked. You can do ::

 $ svn co svn://danse.us/buildInelast/mcvine-1.0beta

and change into the checked-out directory::

 $ cd mcvine-1.0beta


.. _install-src-repo-on-web:

DANSE package repository on the web
"""""""""""""""""""""""""""""""""""
You can get a source distribution of mcvine
from http://dev.danse.us/packages/mcvine-1.0beta-src.tgz. 
You will need
to expand it somewhere::

 $ tar -xvzf mcvine-1.0beta-src.tgz

and change into the expanded directory::

 $ cd mcvine-1.0beta-src


Before you install
^^^^^^^^^^^^^^^^^^
You will need a c++ compiler. You may try this command if you use
a typical linux environment ::

 $ g++

Numpy is required, you could test whether it exists in your system by ::

 $ python
 >>> import numpy

Boost python is required for generating python bindings of mcvine c++ libraries.
Please let mcvine installer know about your boost python installation by ::

 $ export BOOSTPYTHON_DIR=/path/to/boost/python

If you want to take advantage of parallel computing, please install
mpich2. After installation of mpich2, you will need include mpich2 
executables such as mpicxx in your PATH, so that the following
command does not complain about "command not found"::

 $ mpicxx



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

You should see mcvine starting to compile the mcstas E_monitor
component (this will happen only once for every type of 
mcvine-wrapped mcstas component. Built-in mcvine components
don't need this step) and then show some info about the E_monitor
component. If you see anything unexpected, there must be some
problem in the installation; please don't hesitate to post
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


.. _platform-specific-instructions:

Platform specific instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ubuntu 9.10+
""""""""""""

Before install mcvine, please install following packages:
* g++
* python-dev
* libboost-python1.38 (or other version currently in your installation)
* python-numpy
* python-h5py
* python-psutil

Optionally

- ... for parallel mcvine
 * mpich2 
 * libmpich2-dev

- ... for installing from svn
 * subversion


fedora 14
"""""""""

Before install mcvine, please install following packages using package manager
(System->Administration->Add/Remove Software) or yum:

* gcc-c++
* python-devel
* hdf5-devel
* boost-devel, boost-python
* numpy
* python-psutil

And then install h5py using easy_install (as super user)::

 $ easy_install h5py


Optionally

- ... for parallel mcvine
 * mpich2-devel

- ... for installing from svn
 * wget
 * subversion


If using mpich2, need to set the following environment variables::

 $ export MPI_DIR=/usr/lib/mpich2
 $ export MPI_INCDIR=/usr/include/mpich2-i386
 $ export MPI_LIBDIR=$MPI_DIR/lib
 $ export PATH=$MPI_DIR/bin:$PATH


Cent OS 5.5
"""""""""""
Before install mcvine, please install following packages using 
yum:

* gcc-c++
* hdf5-devel (it is not included in standard package repository, so you will need to download the rpm directly, or add extra repository like rpmforge)


python
''''''

You will need to install python 2.6+ from source (default version in Cent OS 5.5 is 2.4 and it does not work for some dependencies of mcvine):

1. Install zlib development package::

 $ yum install zlib-devel


2. Download python source tarball from http://python.org and expand::

 $ tar xvfz <python-tar-ball>
 $ cd Python-x.x.x

3. Configure python and build and install::

 $ ./configure --prefix=<prefix> --with-zlib=/usr/include
 $ make
 $ make install

Then we can install setuptools (easy install) 
from http://pypi.python.org/pypi/setuptools.


numpy
'''''
1. Download source tar ball from numpy: http://numpy.org 
2. Expand::

 $ tar xvzf numpy-x.x.x.tar.gz

3. Build and install

 $ cd numpy-x.x.x
 $ python setup.py install


h5py
''''
Install using easy_install::

 $ easy_install h5py

psutil
''''''
Install using easy_install::

 $ easy_install psutil

boost python
''''''''''''

from source.


Optionally
''''''''''

- ... for parallel mcvine
 * mpich2-devel

- ... for installing from svn
 * subversion




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

 $ source ~linjiao/.mcvine


Systems tested
--------------

* Ubuntu 
 - 9.10
 - 10.04

* Fedora
 - 14

* RHEL client
 - 5.5

* Cent OS
 - 5.5
