#!/usr/bin/env bash

if [ -z "$CORES" ];
    then CORES=2;
fi

PYVER_MAJOR=`python -c "import sys; print sys.version_info[0]"`
PYVER_MINOR=`python -c "import sys; print sys.version_info[1]"`
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}

mkdir build
cd build
cmake -DCONDA_BUILD=TRUE \
      -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX \
      -DPYTHON_LIBRARY=${PREFIX}/lib/libpython${PYVER}.so \
      -DPYTHON_INCLUDE_DIR=${PREFIX}/include/python${PYVER} \
      -DCMAKE_PREFIX_PATH=$PREFIX \
      -DCMAKE_SYSTEM_LIBRARY_PATH=$PREFIX/lib \
      .. \
    && make -j $CORES \
    && make -j$CORES reconfigure-to-include-mcstas-components \
    && make -j$CORES wrap-mcstas-components-cmake \
    && make -j$CORES \
    && make install
