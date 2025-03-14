# To use this env setup script
#
# * git clone mcvine to ~/dv/mcvine/mcvine
# * git clone resources to ~/dv/mcvine/resources
# * install conda
# * create conda environment dev-mcvine-py{VER} with deps. e.g.
#   $ conda create -n dev-mcvine-py36 -c mcvine/label/unstable python=3.6 pyyaml numpy cmake gxx_linux-64=7 psutil h5py mpi4py gsl=2.4 boost=1.66 numpy=1.14.0 danse.ins.numpyext=0.1.3 danse.ins.bpext=0.1.4 histogram=0.3.7 drchops=2.0.3 pyre danse.ins.dsm diffpy.Structure periodictable matplotlib ipython
#
# * activate the environment. e.g.
#   $ . ~/.use-mc3
#   $ source activate dev-mcvine-py36
#
# * Then source this script
#   $ . envs.sh
#
# * Build
#   - first time or restart from fresh: build0
#   - later builds: mm

# build parameter
CORES=12

PREFIX=$CONDA_PREFIX
PYVER_MAJOR=`python -c "from __future__ import print_function; import sys; print(sys.version_info[0])"`
PYVER_MINOR=`python -c "from __future__ import print_function; import sys; print(sys.version_info[1])"`
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}
echo $PYVER
echo $PREFIX

PY_INCLUDE_DIR=${PREFIX}/include/`ls ${PREFIX}/include/|grep python${PYVER}`
PY_SHAREDLIB=${PREFIX}/lib/`ls ${PREFIX}/lib/|grep libpython${PYVER}[a-z]*.so$`
PY_SITE_PKG=${PREFIX}/lib/`ls ${PREFIX}/lib/|grep ^python${PYVER}[a-z]*$`/site-packages
echo $PY_INCLUDE_DIR
echo $PY_SHAREDLIB
echo $PY_SITE_PKG

# SSH agent needed for git
# . ~/.ssh/start-agent

# paths
# update the MCVINE_PKG_ROOT_DIR to point to the directory where mcvine, recources, and other subpackages are cloned at the same level (next to each other)
MCVINE_PKG_ROOT_DIR=$HOME/Projects/MCVine
export MCVINE_SRC=$MCVINE_PKG_ROOT_DIR/mcvine
export MCVINE_RESOURCES=$MCVINE_PKG_ROOT_DIR/resources
export BUILD_ROOT=$MCVINE_PKG_ROOT_DIR/build-$PYVER
export MCVINE_EXPORT_ROOT=$MCVINE_PKG_ROOT_DIR/export-$PYVER
MCVINE_SRC_MCSTAS_COMPONENTS_INTERMEDIATE_DIR=$MCVINE_SRC/packages/legacycomponents/mcstas2/components

# helper functions
mcvine_cmake0 () {
    __SRC_DIR=$1
    __BUILD_DIR=$2
    mkdir -p $__BUILD_DIR
    cd $__BUILD_DIR
    cmake $__SRC_DIR \
	        -DCMAKE_INSTALL_PREFIX=$MCVINE_EXPORT_ROOT \
	        -DDEPLOYMENT_PREFIX=$CONDA_PREFIX \
	        -DCMAKE_SYSTEM_LIBRARY_PATH=$CONDA_PREFIX/lib \
	        -DPYTHON_LIBRARY=$PY_SHAREDLIB \
	        -DPYTHON_INCLUDE_DIR=$PY_INCLUDE_DIR \
	        -DBOOST_ROOT=$CONDA_PREFIX \
#         -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_FLAGS="-D DEBUG"
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
alias clear_intermediate_mcstas_components_dir="cd $MCVINE_SRC_MCSTAS_COMPONENTS_INTERMEDIATE_DIR && rm -rf * && git checkout ."
alias build0="clear_intermediate_mcstas_components_dir && rm -rf $BUILD_ROOT && mkdir $BUILD_ROOT && cd $BUILD_ROOT && mm0 && mmfull"
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

# build subpackages in MCVINE_PKG_ROOT_DIR, including mantid2mcvine
# currently python site-packages are installed in the <build> directory at lib64/
# some of the following subpackages have lib64 and other lib as the python lib directory
# all mcvine-packages should be installed at the same libdir; the process followed is for lib64/
# the opposite subpackages will need to be updated for the lib/ case
# git clone them next to mcvine-core (https://github.com/mcvine/mcvine.git)
# in phonon source code update the CMakeLists.txt INSTALL_LIB_DIR lib64
alias mm_phonon="mcvine_build_subpkg $MCVINE_PKG_ROOT_DIR/phonon $MCVINE_PKG_ROOT_DIR/phonon/build"
alias mm_instruments="mcvine_build_subpkg $MCVINE_PKG_ROOT_DIR/instruments $MCVINE_PKG_ROOT_DIR/instruments/build"
#in workflow source code update the CMakeLists.txt INSTALL_LIB_DIR lib64
alias mm_workflow="mcvine_build_subpkg $MCVINE_PKG_ROOT_DIR/workflow $MCVINE_PKG_ROOT_DIR/workflow/build"
#in ui source code update the CMakeLists.txt INSTALL_LIB_DIR lib64
alias mm_ui="mcvine_build_subpkg $MCVINE_PKG_ROOT_DIR/ui $MCVINE_PKG_ROOT_DIR/ui/build"
#for mantd2mcvine installation from source code
#cd mantid2mcvine
#python setup.py install --prefix=$MCVINE_DIR/ --install-lib=$MCVINE_DIR/lib64/python$PYVER/site-packages/ --single-version-externally-managed --record record.txt

# for usage
export MCVINE_DIR=$MCVINE_EXPORT_ROOT
export EXPORT_ROOT=$MCVINE_EXPORT_ROOT # pyre etc
export PATH=$MCVINE_DIR/bin:$PATH
export PYTHONPATH=$MCVINE_DIR/lib64/python$PYVER/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$MCVINE_DIR/lib64:$LD_LIBRARY_PATH

echo $LD_LIBRARY_PATH


#notes
# since this is a local build/installation
# . envs.sh needs to be executed on the same terminal before running any other scripts that use the local build of mcvine
# the environmental variables above are set to point to the build directory
