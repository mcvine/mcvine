#!/bin/bash

set -x
set -e

#
export PATH=$HOME/mc/bin:$PATH
#
export GIT_FULL_HASH=`git rev-parse HEAD`
export GIT_VER=`git describe --tags`
export VERSION=`git describe --tags | cut -d '-' -f1 | cut -c2-`
export VERSION_NEXT=`echo ${VERSION}| awk -F. -v OFS=. 'NF==1{print ++$NF}; NF>1{if(length($NF+1)>length($NF))$(NF-1)++; $NF=sprintf("%0*d", length($NF), ($NF+1)%(10^length($NF))); print}'`
TIMESTAMP=`date "+%Y%m%d%H%M%S"`
echo $VERSION $VERSION_NEXT
export MCVINE_CONDA_PKG_VER=${VERSION_NEXT}.dev${TIMESTAMP}
echo $MCVINE_CONDA_PKG_VER
cd builders/aws-codebuild/conda-recipe

# create meta.yaml
./create_meta_yaml $MCVINE_CONDA_PKG_VER $GIT_FULL_HASH
grep version meta.yaml
grep git_rev meta.yaml

# build
cat meta.yaml
cat conda_build_config.yaml
conda build --python $PYTHON_VERSION .

# upload
conda env list
conda install anaconda-client
conda list
which anaconda
conda config --set anaconda_upload no
CONDA_ROOT_PREFIX=$(realpath $(dirname `which conda`)/..)
echo $CONDA_ROOT_PREFIX
anaconda -t $ANACONDA_UPLOAD_TOKEN upload --force --label unstable \
         $CONDA_ROOT_PREFIX/conda-bld/linux-64/mcvine-core-$MCVINE_CONDA_PKG_VER-*.tar.bz2
