#!/usr/bin/env bash

./ssd \
    -typos=relaxed \
    -geometer.detector="((-3, 0, 10), (0, 90, 0))" \
    -detector=PSD_TEW_monitor \
    -detector.filename=psdtew.dat \
    -detector.format=table \
    -detector.type=energy \
    -detector.bmin=0 \
    -detector.bmax=100 \
    -detector.deltab=0 \
    -detector.nbchan=10 \
    -detector.nxchan=1 \
    -detector.xwidth=1 \
    -detector.nychan=1 \
    -detector.yheight=1 \
    -ncount=100000 \
    -buffer_size=100000 \
#    -tracer=console


#    -ncount=1e5 \
#    -buffer_size=10000 \

