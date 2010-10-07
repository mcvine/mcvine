#!/usr/bin/env bash


# this test run a tiny sample with a isotropic S(Q,E) kernel and result is
# recorded in a IQE_monitor.
# The plot should show an evenly distributed intensity on the S(Q,E) plot


mcvine-simulate \
    --components=source,sample,monitor \
    --- \
    --overwrite-datafiles \
    --ncount=2e5 \
    --buffer_size=100000 \
    \
    --source=MonochromaticSource \
    --sample=SampleAssemblyFromXml \
    --monitor=IQE_monitor \
    \
    --source.energy=60 \
    \
    --sample.xml=sampleassemblies/Ni-isotropicsqekernel/sampleassembly.xml \
    \
    --monitor.Ei=60 \
    --monitor.Qmin=0. \
    --monitor.Qmax=11. \
    --monitor.nQ=110 \
    --monitor.Emin=-45. \
    --monitor.Emax=45. \
    --monitor.nE=90 \
    

PlotHist.py out/iqe_monitor.h5
