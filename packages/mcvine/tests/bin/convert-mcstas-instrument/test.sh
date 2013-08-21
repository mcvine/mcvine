#!/usr/bin/env sh

mcvine-convert-mcstas-instrument -input=dummy.instr
./config-dummy
./dummy

mcvine-convert-mcstas-instrument -input=dummy2.instr
./config-dummy2
./dummy2
