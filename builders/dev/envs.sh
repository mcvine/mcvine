# this script help set up the env vars for development
#
# Directory structure
# assume mapping:
#   ~/dv/mcvine/<>  -> git clone git@github.com:mcvine/<>
#     * mcvine
#     * resources
# also under ~/dv/mcvine
#     * build: cmake build
#     * export: cmake export

# activate conda environment
source activate dev-mcvine

CPUCOUNT=7

export MCVINE_RESOURCES=$HOME/dv/mcvine/resources
export MCVINE_DIR=$HOME/dv/mcvine/export
export EXPORT_ROOT=$MCVINE_DIR
export PATH=$MCVINE_DIR/bin:$PATH
export PYTHONPATH=$MCVINE_DIR/lib/python2.7/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$MCVINE_DIR/lib:$LD_LIBRARY_PATH

# These aliases should only be run under ~/dv/mcvine/build
# * mm: normal quick build 
# * mmfull: full build including mcstas components
# * mt: run tests
# * mm0: cmake configure
alias mm="cmake ../mcvine && make -j $CPUCOUNT install"
alias mmfull="cmake ../mcvine && make -j $CPUCOUNT && make reconfigure-to-include-mcstas-components && make wrap-mcstas-components-cmake && make install -j $CPUCOUNT"
alias mt='env CTEST_OUTPUT_ON_FAILURE=1 make test ARGS="-j$CPUCOUNT"'
alias mm0="cmake -DCMAKE_INSTALL_PREFIX=$EXPORT_ROOT -DDEPLOYMENT_PREFIX=$CONDA_ENV_PATH -DCMAKE_PREFIX_PATH=$CONDA_ENV_PATH ../mcvine"
