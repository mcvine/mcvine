#!/usr/bin/env bash

mcvine-simulate \
    --components=source,sample,monitor \
    --- \
    --overwrite-datafiles \
    --source=MonochromaticSource \
    --monitor=E_monitor \
    \
    --source.energy=60 \
    --monitor.Emin=50 \
    --monitor.Emax=70 \
    --monitor.nchan=100 \
    

# help
#mcvine-simulate \
#    --components=source,sample,monitor \
#    --- \
#    --source=MonochromaticSource \
#    --monitor=E_monitor \
#    \
#    --help-components \
#    --source.help-properties \
#    --monitor.help-properties \
 

PlotHist.py out/e.h5