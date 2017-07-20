#!/usr/bin/env bash

if [ $# -eq 0 ]
then
    echo "Usage: ./builders/build <src-path> <build-path> <install-path> <resources-path> [cores]"
    echo
    echo "Example: ./builders/build \$PWD \$PWD/build \$PWD/install \$PWD/resources 20"
    echo
    exit 1
fi

SRC=$1
BUILD=$2
INSTALL=$3
export MCVINE_RESOURCES=$4

CORES=$5
if ((CORES < 1)); then
    let CORES=`grep -c ^processor /proc/cpuinfo`
    let CORES-=1
    if ((CORES < 1)); then
	CORES = 1;
    fi
fi

echo "Building mcvine"
echo "- mcvine resoureces: $MCVINE_RESOURCES"
echo "- using $CORES cores"

source $HOME/fermi/mcvine/.build-mcvine

rm -rf $BUILD
mkdir $BUILD
cd $BUILD
cmake \
    -D PYTHON_LIBRARY=/sw/fermi/python27/2.7.5/rhel6.3_gnu4.4.6/lib/libpython2.7.so \
    -D PYTHON_INCLUDE_DIR=/sw/fermi/python27/2.7.5/rhel6.3_gnu4.4.6/include/python2.7 \
    -D Boost_NO_BOOST_CMAKE=yes \
    -D DEPLOYMENT_PREFIX=$INSTALL \
    -D CMAKE_INSTALL_PREFIX=$INSTALL \
    $SRC \
    && make -j$CORES reconfigure-to-include-mcstas-components \
    && MCVINE_MPI_BINDING=NONE make -j$CORES wrap-mcstas-components-cmake \
    && make -j$CORES 

#   -D GSL_HOME=/usr/common/usg/gsl/1.16/gnu \
#   -D BOOST_ROOT=/usr/common/usg/boost/1.54.0-20160127/gnu \
#   -D BOOST_INCLUDEDIR=/usr/common/usg/boost/1.54.0-20160127/gnu/include \
