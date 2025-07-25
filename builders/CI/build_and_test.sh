#!/bin/bash

set -x
set -e
#
CURRENT_BRANCH=$GITHUB_HEAD_REF
echo "Current branch: $CURRENT_BRANCH"
export GIT_FULL_HASH=`git log -1 --format=%H`
export GIT_VER=`git describe --tags`
export VERSION=`git describe --tags | cut -d '-' -f1 | cut -c2-`
export VERSION_NEXT=`echo ${VERSION}| awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}'`
echo $VERSION $VERSION_NEXT
export MCVINE_CONDA_PKG_VER=${VERSION_NEXT}.dev
echo $MCVINE_CONDA_PKG_VER
cd builders/CI/conda-recipe

# build
cat meta.yaml
cat conda_build_config.yaml
echo "Conda environment packages"
micromamba list
cd ../
pwd
conda build --no-test .
#install conda package
conda install -y -c conda-forge conda-build conda-index
python -m conda_index ${CONDA_PREFIX}/conda-bld/
conda install -y -c ${CONDA_PREFIX}/conda-bld/ mcvine-core
#test package
mcvine test