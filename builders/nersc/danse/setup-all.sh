#!/usr/bin/env bash

PKGS=danse.ins numpyext bpext dsm matter journal pyre histogram

for pkg in $PKGS; do
    ./setup.sh $PKG;
done

./setup.sh drchops 2-alpha