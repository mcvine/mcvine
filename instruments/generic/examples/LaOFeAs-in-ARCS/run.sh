#!/usr/bin/env bash
rm -rf out-*
ncount=1e7
buffer_size=100000
np=5

rm -rf out-* 
SSSD.py --mpirun.nodes=${np} -ncount=${ncount} -buffer_size=${buffer_size}
