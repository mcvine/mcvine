# Setup MCViNE dev env using an AWS instance

* start an instance from a miniconda AMI 
  - c3.xlarge
  - ssh-only
* updated authorized_keys

Install dependencies
* sudo apt-get update
* sudo apt-get install git build-essential
* conda create -n dev-mcvine python
* source activate dev-mcvine
* conda config --add channels conda-forge 
* conda config --add channels mcvine
* conda install mcvine-resources
* conda install pyyaml numpy h5py psutil mpi4py gsl boost cmake
* conda install pyre danse.ins.numpyext danse.ins.bpext danse.ins.dsm histogram danse.ins.matter drchops

Also 
* conda install scipy matplotlib

Then mcvine itself
* mkdir dv
* cd dv
* git clone git@github.com:mcvine/mcvine
* git clone git@github.com:mcvine/resources
* mkdir build
* cd build
* cmake -DCMAKE_SYSTEM_LIBRARY_PATH=/home/ubuntu/miniconda2/envs/dev-mcvine/lib/ -DDEPLOYMENT_PREFIX=/home/ubuntu/miniconda2/envs/dev-mcvine -DCMAKE_INSTALL_PREFIX=~/dv/export ../mcvine/


## The .dev-mcvine file

```
source activate dev-mcvine

CPUCOUNT=4

export PYVER=2.7
#export DEPLOYMENT_PREFIX=${CONDA_ENV_PATH}

export MCVINE_RESOURCES=$HOME/dv//resources
export MCVINE_DIR=$HOME/dv/export
export EXPORT_ROOT=$MCVINE_DIR # pyre etc
export PATH=$MCVINE_DIR/bin:$PATH
export PYTHONPATH=$MCVINE_DIR/lib/python${PYVER}/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$MCVINE_DIR/lib:$LD_LIBRARY_PATH

alias mm="cmake ../mcvine && make -j $CPUCOUNT && make -j $CPUCOUNT install"
alias mmfull="cmake ../mcvine && make -j $CPUCOUNT && make reconfigure-to-include-mcstas-components && make wrap-mcstas-components-cmake && make install -j $CPUCOUNT"
alias mt='env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j$CPUCOUNT"'
```


* use mmfull alias to build
* use mt alias to test
