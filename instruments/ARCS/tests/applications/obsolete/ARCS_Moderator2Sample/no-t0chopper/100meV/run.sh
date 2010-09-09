#!/usr/bin/env bash
node=n04
packetsize=100
ncount=5e7
buffersize=100000

rsh -. $node "rm -rf neutrons.dat && ARCS_Moderator2Sample.py --neutron_recorder.packetsize=$packetsize -ncount=$ncount -buffer_size=$buffersize -overwrite-datafiles"
