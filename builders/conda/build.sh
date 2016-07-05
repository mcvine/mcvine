#!/usr/bin/env bash

PYVER_MAJOR=${CONDA_PY:0:1}
PYVER_MINOR=${CONDA_PY:1:1}
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}

let CORES=`grep -c ^processor /proc/cpuinfo`
let CORES-=1
if ((CORES < 1)); then
    CORES=1;
fi
CORES=2

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX -DPYTHON_LIBRARY=${PREFIX}/lib/libpython${PYVER}.so -DPYTHON_INCLUDE_DIR=${PREFIX}/include/python${PYVER} .. && make -j $CORES && make -j$CORES reconfigure-to-include-mcstas-components && make -j$CORES wrap-mcstas-components-cmake && make -j$CORES && make install
