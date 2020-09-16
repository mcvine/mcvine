#!/bin/bash

cd $HOME
# conda
wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b -p $HOME/mc
export PATH=$HOME/mc/bin:$PATH
which conda
