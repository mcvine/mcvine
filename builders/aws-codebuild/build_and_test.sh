#!/bin/bash

set -x
export PATH=$HOME/mc/bin:$PATH
export GIT_FULL_HASH=`git rev-parse HEAD`
export GIT_VER=`git describe --tags`
export VERSION="1.3.5"
echo $VERSION
export MCVINE_CONDA_PKG_VER=${VERSION}unstable
echo $MCVINE_CONDA_PKG_VER
cd builders/aws-codebuild/conda-recipe
./create_meta_yaml $MCVINE_CONDA_PKG_VER $GIT_FULL_HASH
grep version meta.yaml
grep git_rev meta.yaml
cat meta.yaml
cat conda_build_config.yaml
conda build --python $PYTHON_VERSION .
