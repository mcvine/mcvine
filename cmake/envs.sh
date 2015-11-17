# this script help set up the env vars for development
# run this at the root of the mcvine source tree

. /opt/danse/bin/setup-danse.sh
export MCVINE_RESOURCES=~/dv/mcvine/resources

EXPORT_ROOT=$PWD/build/export
export PATH=$EXPORT_ROOT/bin:$PATH
export PYTHONPATH=$EXPORT_ROOT/python:$PYTHONPATH
export LD_LIBRARY_PATH=$EXPORT_ROOT/lib:$LD_LIBRARY_PATH
export MCVINE_DIR=$EXPORT_ROOT
