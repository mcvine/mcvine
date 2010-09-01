#!/usr/bin/env bash

# get help
mcvine-simulate -h | more

# specify the names of components in the instrument
mcvine-simulate -components=source,monitor

# specify the component types 
mcvine-simulate -components=source,monitor --- -source=Source_simple -monitor=E_monitor

# to see what are the availabe components
mcvine-list-components
mcvine-list-components -category=sources

# to specify the number of "neutrons" run in the simulation
mcvine-simulate -components=source,monitor --- -source=Source_simple -monitor=E_monitor -ncount=1e6 --overwrite-datafiles

# to see a plot of the monitor data
PlotHist.py out/IE.h5
