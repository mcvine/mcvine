#!/usr/bin/env python

from mcvine import run_script
run_script.run_mpi('./ARCS_10_25_2008_mcvine_revised.py', 'out.testrun', ncount=1e7, nodes=20, overwrite_datafiles=True)
