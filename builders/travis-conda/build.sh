#!/usr/bin/env bash

if [ -z "$CORES" ];
    then CORES=2;
fi

PYVER_MAJOR=${CONDA_PY:0:1}
PYVER_MINOR=${CONDA_PY:1:1}
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}

mkdir build
cd build
# somehow in conda build at travis machine, cmake finds
# python 3 instead of python 2, even when -DCMAKE_SYSTEM_LIBRARY_PATH=$PREFIX
# is used.
cmake \
    -DCMAKE_INSTALL_PREFIX=$PREFIX \
    -DDEPLOYMENT_PREFIX=$PREFIX \
    -DPYTHON_LIBRARY=${PREFIX}/lib/libpython${PYVER}.so \
    -DPYTHON_INCLUDE_DIR=${PREFIX}/include/python${PYVER} \
    .. \
    && make -j$CORES \
    && make -j$CORES reconfigure-to-include-mcstas-components \
    && make -j$CORES wrap-mcstas-components-cmake \
    && make -j$CORES && make install
