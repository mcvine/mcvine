#!/usr/bin/env sh

./Nickel.py \
    --ncount=100000 \
    --buffer_size=10000 \
    --output-dir=out \
    --overwrite-datafiles 


./events2Idpt.py

cp Idpt.h5 reduction/main
cd reduction && MCSimReductionApp.py && cd ..


PlotHist.py reduction/sqehist.pkl
