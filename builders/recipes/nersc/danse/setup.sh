#!/usr/bin/env bash
PKG=$1
BRANCH=$2

git clone git@github.com:danse-inelastic/$PKG
cd $PKG

if [ "$BRANCH" != "" ];
  then
    git checkout $BRANCH;
fi

mkdir build
cd build
cmake -D CMAKE_C_COMPILER=/opt/gcc/5.2.0/bin/gcc \
    -D CMAKE_CXX_COMPILER=/opt/gcc/5.2.0/bin/g++ \
    -D PYTHON_LIBRARY=/usr/common/usg/python/2.7.9/lib/libpython2.7.so \
    -D PYTHON_INCLUDE_DIR=/usr/common/usg/python/2.7.9/include/python2.7 \
    -D CMAKE_INSTALL_PREFIX=$HOME/dv/danse/export \
    -D DEPLOYMENT_PREFIX=$HOME/dv/danse/export \
    ..
make install


#   -D BOOST_INCLUDEDIR=$BOOST_DIR/include \
