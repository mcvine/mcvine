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

# For development
alias mi="cd $BUILD_ROOT; make install"
alias mm="cd $BUILD_ROOT; cmake ../mcvine && make -j $CORES && make -j $CORES install"
alias mmfull="cd $BUILD_ROOT; cmake ../mcvine && make -j $CORES && make reconfigure-to-include-mcstas-components && make wrap-mcstas-components-cmake && make install -j $CORES"
alias mt='cd $BUILD_ROOT; env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j$CORES"'
#   first time build
alias mm0="cmake $MCVINE_SRC -DCMAKE_INSTALL_PREFIX=$MCVINE_EXPORT_ROOT -DDEPLOYMENT_PREFIX=$CONDA_PREFIX"
alias build0="rm -rf $BUILD_ROOT && mkdir $BUILD_ROOT && cd $BUILD_ROOT && mm0 && mmfull"

# for users
export MCVINE_DIR=$MCVINE_EXPORT_ROOT
export EXPORT_ROOT=$MCVINE_EXPORT_ROOT # pyre etc
export PATH=$MCVINE_DIR/bin:$PATH
export PYTHONPATH=$MCVINE_DIR/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$MCVINE_DIR/lib:$LD_LIBRARY_PATH
