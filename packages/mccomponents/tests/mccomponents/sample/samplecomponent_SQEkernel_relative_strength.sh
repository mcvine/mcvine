#!/usr/bin/env bash

# This test runs two simulations. Both uses two SQEkernels: one with a uniformly distributed
# SQE in a large Q, E range, another with intensities only around elastic line.
# In the first simulation below, the "elastic line" has the same intensity as the
# uniformly distributed SQE;
# while in the second simulation, the "elastic line" has much stronger intensity.
# The simulated I(Q,E) spectra should reflect that.

# clean up
rm -rf out.sqekernel*

# change sqe histogram used in the kernel
ln -sf fake-elastic-line.h5 sampleassemblies/Ni-sqekernel/elastic-line.h5
time ./sqekernel-testapp.py --ncount=1e7 --mpirun.nodes=20 --output-dir=out.sqekernel.even
plothist out.sqekernel.even/iqe_monitor.h5

ln -sf fake-elastic-line-intense.h5 sampleassemblies/Ni-sqekernel/elastic-line.h5
time ./sqekernel-testapp.py --ncount=1e7 --mpirun.nodes=20 --output-dir=out.sqekernel.contrast
plothist out.sqekernel.contrast/iqe_monitor.h5
