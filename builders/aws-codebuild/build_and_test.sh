#!/bin/bash

export PATH=$HOME/mc/bin:$PATH
export GIT_FULL_HASH=`git rev-parse HEAD`
export GIT_VER=`git describe --tags`
export VERSION=`python -c "print('$GIT_VER'.split('-')[0][1:])"`
echo $VERSION
export MCVINE_CONDA_PKG_VER=${VERSION}unstable
echo $MCVINE_CONDA_PKG_VER
cd builders/travis-conda
./create_meta_yaml $MCVINE_CONDA_PKG_VER $GIT_FULL_HASH
grep version meta.yaml
grep git_rev meta.yaml
CORES=2
conda build --numpy=1.16 .
