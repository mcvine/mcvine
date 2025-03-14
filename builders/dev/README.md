# Setup development environment
In this section, we describe the process of installing mcvine-core and related mcvine subpackages in the same conda environment and build directories.

## Checkout src in the local directory
Create a directory and clone inside the mcvine-core and any other mcvine subpackages needed.

Example project location: ~/MCVine

```
$ mkdir -p ~/MCVine/build (the build/ directory is optional)
$ cd ~/MCVine
$ git clone git@github.com:mcvine/mcvine.git
$ git clone git@github.com:mcvine/resources.git
$ git clone git@github.com:mcvine/instruments.git
$ git clone git@github.com:mcvine/workflow.git
$ git clone git@github.com:mcvine/ui.git
$ git clone git@github.com:mcvine/mantid2mcvine.git
```

If only mcvine-core is need, mcvine.git should be cloned and the rest can be skipped.
However, all the above are required for cases like here [MCViNE training with jupyter notebooks](https://github.com/mcvine/training).
May need to clone other mcvine subpackages.

## Create a conda environment with the required dependencies

In the mcvine.git repository navigate

```
$ cd builders/dev/
$ conda env create -f mcvine-dev.yml
$ conda activate mcvine-developer
```

Alternativelly, you can create an empty conda environment and install the depedencies there.
```
$ conda create -n mcvine-developer python=3
$ conda install <deps>
```

The full list of dependencies can be found in 
https://github.com/mcvine/conda-recipes/blob/master/mcvine-core/meta.yaml


## Activate the new env

```
$ source activate mcvine-developer
```

## Run envs var shell script

In this directory's [envs.sh](envs.sh) file update the *MCVINE_PKG_ROOT_DIR* variable to point to the project location, 
example: MCVINE_PKG_ROOT_DIR=$HOME/MCVine

*You can either use the same envs.sh (and avoid commit/push any changes related to the directory path) or copy this one.

Run the script on the terminal

```
$ . envs.sh
```
Add it to .bashrc if needed.

The envs var shell script sets environment variables and command aliases to build mcvine-core and the mcvine subpackages listed above targeting a local path build/installation.
Provided no .bashrc configurations added, the above command should be executed in the envs.sh directory on the same conda environment and terminal before using mcvine.

## Build and install mcvine-core for the first time

```
$ build0
```

## Build
```
$ mm
```

## Install
```
$ mi
```

## Test
```
$ mt

```
*Currently 7/299 tests are failing: [jclemons555-README](https://github.com/jclemons555/mcvine/blob/master/README.md)

## Build/install subpackages from source code
During the mcvine-core building process, \<build\> and \<export\> directories are created and various artifacts are included.

Mcvine-core's python packages are included in the <export>/lib64/ directory (*<export>/lib64/python3.10/site-packages/*). All mcvine packages should be installed at the same location. In every mcvine subpackage, ensure that the if *INSTALL_LIB_DIR* is defined in the CMakeLists.txt file, it points to lib64 (instead of lib) directory:

set(INSTALL_LIB_DIR lib**64** CACHE PATH "Installation directory for libraries")


Regarding the mcvine subpackages listed above, update the CMakeLists.txt of: phonon, workflow and ui with the above change.
In case a mcvine supackage is installed as a python package set the installation library flag to the lib64 directory, e.g. for mantid2mcvine: 
--install-lib=$MCVINE_DIR/lib64/python$PYVER/site-packages/

*If lib/ is the preferable path, the lib64 references in mcvine-core/packages should be updated, instead. (not tested)

After the lib directories are set, run the following commands to build phonon, instruments, workflow and ui
```
$ mm_phonon
$ mm_instruments
$ mm_workflow
$ mm_ui
```

For mantid2mcvine enter the repository's source code
```
$ cd mantid2mcvine
$ python setup.py install --prefix=$MCVINE_DIR/ --install-lib=$MCVINE_DIR/lib64/python$PYVER/site-packages/ --single-version-externally-managed --record record.txt
```

