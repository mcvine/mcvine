#!/usr/bin/env bash

# clean up
rm -rf out.sqekernel*

# change sqe histogram used in the kernel
ln -sf fake-elastic-line.h5 sampleassemblies/Ni-sqekernel/elastic-line.h5
time ./sqekernel-testapp.py --ncount=1e7 --mpirun.nodes=20 --output-dir=out.sqekernel.even
plothist out.sqekernel.even/iqe_monitor.h5

ln -sf fake-elastic-line-intense.h5 sampleassemblies/Ni-sqekernel/elastic-line.h5
time ./sqekernel-testapp.py --ncount=1e7 --mpirun.nodes=20 --output-dir=out.sqekernel.contrast
plothist out.sqekernel.contrast/iqe_monitor.h5
