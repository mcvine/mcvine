#!/bin/bash

cd `dirname "$0"`
# cd builders/travis-conda
./create_meta_yaml $MCVINE_CONDA_PKG_VER $GIT_FULL_HASH
grep version meta.yaml
grep git_rev meta.yaml
export ERRLOG=/home/travis/build/log.error
echo "ERRLOG=" $ERRLOG
export CORES=1
conda build --python=$TRAVIS_PYTHON_VERSION .
