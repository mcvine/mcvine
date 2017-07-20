#!/usr/bin/env bash

rm -rf out 
rm -f *.pml
sequoia-m2s -E=100 --- -h -dump-pml

MODFILE=`python -c "from mcvine import resources as r; import os; print os.path.join(r.instrument('SEQUOIA'), 'moderator', 'source_sct521_bu_17_1.dat')"`
sequoia-moderator2sample --ncount=1e7 --mod.S_filename=$MODFILE
