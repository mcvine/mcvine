#!/usr/bin/env bash

rm -rf out 
rm -f *.pml
sequoia-m2s -E=100 --- -h -dump-pml
sequoia-moderator2sample --ncount=1e7
