.. _installation:

Installation
============

For a list of systems deployed with MCViNE, please go to
:ref:`deployments <deployments>`.

At this moment, mcvine can only be installed from source.

Build mcvine from svn source
----------------------------



Before you install
^^^^^^^^^^^^^^^^^^
This installation requires that you have installed subversion and have
a  c++ compiler. It is also necessary for your system admin to allow
you to check out svn repository of danse anonymously  (At some places,
this is blocked.); you can try the following command to see if it works::

 $ svn co -N svn://danse.us/buildInelast/mcvine

Also you will need a c++ compiler. You may try this command if you use
a typical linux environment ::

 $ g++


Build and Install
^^^^^^^^^^^^^^^^^

To start, check out a release builder from danse.us svn repo::

 $ svn co svn://danse.us/buildInelast/mcvine

Then get all sources::

 $ cd mcvine
 $ ./getsrc.py

Then build::

 $ ./build.py

If everything goes fine. You will have a mcvine installation built
under directory "EXPORT"::

 $ ls EXPORT

will output something like::

 bin  deps  docs  etc  include  lib  modules  share


.. _deployments:

Deployments
===========

DANSE clusters at Caltech CACR
------------------------------

foxtrot.danse.us
^^^^^^^^^^^^^^^^
MCViNE is available through the "modules" package manager.

To use mcvine, run ::

 $ module add python wx mcvine



ARCS clusters at SNS
--------------------
MCViNE is tentatively installed on arcs clusters at SNS. 
You can use it at arcs1 and arcs2 clusters.

To use mcvine, run ::

 $ source ~linjiao/.mcvine

