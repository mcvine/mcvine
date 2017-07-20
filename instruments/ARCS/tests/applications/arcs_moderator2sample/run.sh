#!/usr/bin/env bash

LAUNCHER=`python -c "from mcni.pyre_support.MpiApplication import mpi_launcher_choice as l; print l"`

rm -rf out
mcvine instruments arcs mod2sample --moderator.S_filename=$MCVINE_RESOURCES/instruments/ARCS/moderator/source_sct521_bu_17_1.dat --ncount=1e6 --buffer_size=100000 --${LAUNCHER}.nodes=2
