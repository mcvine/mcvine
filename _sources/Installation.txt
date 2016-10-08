.. _installation:

Installation
============

MCViNE can be installed in most of recent linux distributions by using conda::

 $ conda create -n mcvine python             # create an environment for mcvine
 $ source activate mcvine                    # activate mcvine environment
 $ conda config --add channels conda-forge   # add conda channels
 $ conda config --add channels mcvine
 $ conda install mcvine                      # install

To install conda on a linux distribution, please refer to 
`miniconda quick install <http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install>`_.

.. For a list of systems already deployed with MCViNE, please go to
.. :ref:`deployments <deployments>`.


If you want to build mcvine from source,
please refer to
`the mcvine conda recipes <https://github.com/mcvine/conda-recipes>`_.


Install the latest unstable build
---------------------------------

Latest build of mcvine can be installed by 
 $ conda install -c mcvine/label/unstable mcvine
