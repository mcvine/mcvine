#!/usr/bin/env bash

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# This is obsolete. Just follow what is in .travis.yml
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# simulate the travis environment
# run under ~/dv/mcvine/travis-CI/mcvine
# ./builders/sim-travis.sh <branch>

# update and pull the branch
git checkout master
git pull
git checkout $1
git pull

# update resources
cd resources
git pull
cd ..

echo "************************************************************************"
echo "*** Will start docker image. "
echo
echo Inside the docker, run
echo
echo  $ ./builders/build /mcvine-src /mcvine-build /mcvine-install /mcvine-src/resources
echo
echo to build.
echo
echo Then run
echo
echo  $ export MCVINE_RESOURCES=/mcvine-src/resources 
echo  $ . /opt/danse/bin/setup-danse.sh 
echo  $ cd /mcvine-build/
echo
echo to get ready for testing.
echo
echo Run
echo
echo  $ ctest -R testname -V
echo
echo to test
echo "************************************************************************"

# start the docker image
docker run -it -v $PWD:/mcvine-src -w /mcvine-src linjiao/mcvine-ubuntu-deps:14.04 bash


