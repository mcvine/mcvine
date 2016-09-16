#!/usr/bin/env bash

if [ -z "$CORES" ];
    then CORES=2;
fi

PYVER_MAJOR=${CONDA_PY:0:1}
PYVER_MINOR=${CONDA_PY:1:1}
PYVER=${PYVER_MAJOR}.${PYVER_MINOR}

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DCMAKE_SYSTEM_LIBRARY_PATH=$PREFIX .. \
    && make -j$CORES \
    && make -j$CORES reconfigure-to-include-mcstas-components \
    && make -j$CORES wrap-mcstas-components-cmake \
    && make -j$CORES && make install

