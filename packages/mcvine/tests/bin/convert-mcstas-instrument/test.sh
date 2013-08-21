#!/usr/bin/env sh

rm -rf out

mcvine-convert-mcstas-instrument -input=dummy.instr
./config-dummy --Emin=30.5
./dummy

mcvine-convert-mcstas-instrument -input=dummy2.instr
./config-dummy2 --Edes=100 --E_min=50 --E_max=200 --Heusler
./dummy2
