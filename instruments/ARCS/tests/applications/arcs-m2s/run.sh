#!/usr/bin/env bash

rm -f out/neutrons 
arcs-m2s -E=60 --- --ncount=1e6 --buffer_size=100000 --overwrite-datafiles  2> err
