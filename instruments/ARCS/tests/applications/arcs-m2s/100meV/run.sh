#!/usr/bin/env bash

# --mpirun.nodes option does not work even if we add it after ---
# arcs-m2s is better used just for generation of pml file
# for arcs_moderator2sample.

rm -rf out
mcvine instruments arcs m2s -E=100 --- --moderator.S_filename=$MCVINE_RESOURCES/instruments/ARCS/moderator/source_sct521_bu_17_1.dat --ncount=1e6 --buffer_size=100000 --overwrite-datafiles  2> err
