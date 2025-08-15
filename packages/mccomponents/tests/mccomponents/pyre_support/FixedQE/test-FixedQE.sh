#!/usr/bin/env sh

./FixedQE.py \
    --ncount=10000 \
    --buffer_size=1000 \
    --output-dir=test1_out \
    --overwrite-datafiles 


./events2Idpt.py


cp Idpt.h5 reduction/main
cd reduction && MCSimReductionApp.py && cd ..


# after reduction the S(Q,E) should only have one bright spot at (5, 30)
./assertQEspot.py

