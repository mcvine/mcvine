.. _installation:

Installation
============

.. For a list of systems already deployed with MCViNE, please go to
.. :ref:`deployments <deployments>`.


.. _install_using_pkg_mgr:

Install using package managers
------------------------------

Ubuntu 14.04
~~~~~~~~~~~~

Install::

 $ sudo apt-get update
 $ sudo apt-get install -qy curl
 $ curl -s https://packagecloud.io/install/repositories/danse/ins/script.deb.sh | sudo bash
 $ sudo apt-get install mcvine

Run::

 $ . /opt/danse/bin/setup-mcvine.sh
 $ mcvine


Fedora 21 or CentOS 7
~~~~~~~~~~~~~~~~~~~~~

Install::

 $ sudo yum install -y curl
 $ curl -s https://packagecloud.io/install/repositories/danse/ins/script.rpm.sh | sudo bash
 $ sudo yum install mcvine

Run::

 $ . /opt/danse/bin/setup-mcvine.sh
 $ export PATH=/usr/lib64/mpich/bin:$PATH
 $ export LD_LIBRARY_PATH=/usr/lib64/mpich/lib:$LD_LIBRARY_PATH
 $ export PYTHONPATH=/usr/lib64/python2.7/site-packages/mpich:$PYTHONPATH
 $ mcvine


Build mcvine from source
------------------------

.. note::
   `Docker <https://www.docker.com/>`_ is used to test
   installation of MCViNE on various Linux systems.
   Related Dockerfiles can be found in
   https://github.com/mcvine/mcvine/tree/master/builders/docker
   and they can be used as hints for installing dependencies
   and then building mcvine.
