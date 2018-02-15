# Be careful with this.
# If using ubuntu 16.04 or older, the default gcc is 5.4.0
# mcvine needs 4.*.
# So before building mcvine, have to do the switch by
#  $ sudo update-alternatives --config gcc
#  $ sudo update-alternatives --config g++
# And after the build, have to switch back running the similar cmds

# SSH agent needed for git
. ~/.ssh/start-agent

# paths
export MCVINE_SRC=$HOME/dv/mcvine/mcvine
export MCVINE_RESOURCES=$HOME/dv/mcvine/resources
export BUILD_ROOT=$HOME/dv/mcvine/build
export MCVINE_EXPORT_ROOT=$HOME/dv/mcvine/export

# build parameter
CORES=30

# conda env
. ~/.use-miniconda2
source activate dev-mcvine

# helper functions
mcvine_cmake0 () {
    __SRC_DIR=$1
    __BUILD_DIR=$2
    cd $__BUILD_DIR
    cmake $__SRC_DIR \
	  -DCMAKE_INSTALL_PREFIX=$MCVINE_EXPORT_ROOT \
	  -DDEPLOYMENT_PREFIX=$CONDA_PREFIX \
	  -DCMAKE_SYSTEM_LIBRARY_PATH=$CONDA_PREFIX/lib \
	  -DPYTHON_LIBRARY=${CONDA_PREFIX}/lib/libpython${PYVER}.so \
	  -DPYTHON_INCLUDE_DIR=${CONDA_PREFIX}/include/python${PYVER} \
	  -DBOOST_ROOT=$CONDA_PREFIX
    cd -
}
mcvine_build_subpkg () {
    __SRC_DIR=$1
    __BUILD_DIR=$2
    mcvine_cmake0 $__SRC_DIR $__BUILD_DIR
    cd $__BUILD_DIR; make install; cd -
}

# For development
# clean up everything and build everything
alias build0="rm -rf $BUILD_ROOT && mkdir $BUILD_ROOT && cd $BUILD_ROOT && mm0 && mmfull"
# run cmake for the first time
alias mm0="mcvine_cmake0 $MCVINE_SRC $BUILD_ROOT"
# full build including wrapping mcstas components
alias mmfull="cd $BUILD_ROOT; cmake ../mcvine && make -j $CORES && make reconfigure-to-include-mcstas-components && make wrap-mcstas-components-cmake -j $CORES && make install -j $CORES; cd -"
# partial build. most-used cmd
alias mm="cd $BUILD_ROOT; cmake ../mcvine && make -j $CORES && make -j $CORES install; cd -"
# install
alias mi="cd $BUILD_ROOT; make install; cd -"
# test
alias mt='cd $BUILD_ROOT; env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j$CORES"; cd -'
# build subpackages
alias mm_phonon="mcvine_build_subpkg $HOME/dv/mcvine/phonon $HOME/dv/mcvine/phonon/build"
alias mm_instruments="mcvine_build_subpkg $HOME/dv/mcvine/instruments $HOME/dv/mcvine/instruments/build"
alias mm_workflow="mcvine_build_subpkg $HOME/dv/mcvine/workflow $HOME/dv/mcvine/workflow/build"

# for usage
export MCVINE_DIR=$MCVINE_EXPORT_ROOT
export EXPORT_ROOT=$MCVINE_EXPORT_ROOT # pyre etc
export PATH=$MCVINE_DIR/bin:$PATH
export PYTHONPATH=$MCVINE_DIR/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$MCVINE_DIR/lib:$LD_LIBRARY_PATH
