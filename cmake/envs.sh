. /opt/danse/bin/setup-danse.sh

EXPORT_ROOT=$PWD/build/export
export PATH=$EXPORT_ROOT/bin:$PATH
export PYTHONPATH=$EXPORT_ROOT/python:$PYTHONPATH
export LD_LIBRARY_PATH=$EXPORT_ROOT/lib:$LD_LIBRARY_PATH
export MCVINE_DIR=$EXPORT_ROOT
