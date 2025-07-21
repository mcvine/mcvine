#!/bin/bash

set -x
set -e
echo "Running build_and_test.sh"
#
export PATH=$HOME/mc/bin:$PATH
#
export GIT_FULL_HASH=`git rev-parse HEAD`
export GIT_VER=`git describe --tags`
export VERSION=`git describe --tags | cut -d '-' -f1 | cut -c2-`
export VERSION_NEXT=`echo ${VERSION}| awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}'`
echo $VERSION $VERSION_NEXT
export MCVINE_CONDA_PKG_VER=${VERSION_NEXT}.dev
echo $MCVINE_CONDA_PKG_VER
cd builders/CI/conda-recipe

# create meta.yaml
./create_meta_yaml $MCVINE_CONDA_PKG_VER $GIT_FULL_HASH
grep version meta.yaml
grep git_rev meta.yaml

# configure openmpi to allow run as root
if [ ${CI_NAME} == "aws-codebuild" ]; then
    export OMPI_ALLOW_RUN_AS_ROOT=1
    export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
    echo "localhost slots=8" > $(dirname $(dirname $(which python)))/etc/openmpi-default-hostfile
fi

# build
cat meta.yaml
cat conda_build_config.yaml
echo "Conda environment packages"
micromamba info
micromamba list
cd ../
pwd
conda build --no-test .