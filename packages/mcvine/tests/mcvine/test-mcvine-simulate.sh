#!/usr/bin/env bash

mcvine-simulate \
    --components=source,sample,monitor \
    --- \
    --overwrite-datafiles \
    --source=MonochromaticSource \
    --monitor=E_monitor \
    \
    --source.energy=60 \
    --monitor.Emin=50.5 \
    --monitor.Emax=69.5 \
    --monitor.nchan=19 \
    

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
 

plothist out/IE.h5
