.. _installation:

Installation
============

MCViNE can be installed in most of recent linux distributions by using conda

.. code-block:: shell
		
 $ conda create -n mcvine python=3.6         # create an environment for mcvine
 $ source activate mcvine                    # activate mcvine environment
 $ conda config --add channels conda-forge   # add conda channels
 $ conda config --add channels diffpy
 $ conda config --add channels mantid
 $ conda config --add channels mcvine
 $ conda install mcvine

To install conda on a linux distribution, please refer to 
`miniconda quick install <http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install>`_.

.. For a list of systems already deployed with MCViNE, please go to
.. :ref:`deployments <deployments>`.


If you want to build mcvine from source,
please refer to
`the mcvine conda recipes <https://github.com/mcvine/conda-recipes>`_.

Optional dependencies
---------------------

If we want to use MCPL data files from mcstas simulations, `mcpl` python
package need to be installed ($ pip install mcpl).

Other packages that may be useful

* lmfit
* tqdm
* awscli


Install the latest unstable build
---------------------------------

Latest build of mcvine can be installed by

.. code-block:: shell
		
 $ conda install -c mcvine/label/unstable mcvine python=3.6
