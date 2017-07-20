#!/usr/bin/env bash
PKG=$1
BRANCH=$2

git clone https://github.com/danse-inelastic/$PKG
cd $PKG

if [ "$BRANCH" != "" ];
  then
    git checkout $BRANCH;
fi

mkdir build
cd build
cmake \
    -D PYTHON_LIBRARY=/sw/fermi/python27/2.7.5/rhel6.3_gnu4.4.6/lib/libpython2.7.so \
    -D PYTHON_INCLUDE_DIR=/sw/fermi/python27/2.7.5/rhel6.3_gnu4.4.6/include/python2.7 \
    -D Boost_NO_BOOST_CMAKE=yes \
    -D CMAKE_INSTALL_PREFIX=$HOME/fermi/mcvine/export \
    -D DEPLOYMENT_PREFIX=$HOME/fermi/mcvine/export \
    ..
make install


#   -D BOOST_INCLUDEDIR=$BOOST_DIR/include \
