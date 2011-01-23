#!/usr/bin/env gnuplot -persist

set xrange [45:75]
set term wxt 0
plot "e_monitor1_2.txt" with lines

set xrange [800:1000]
set term wxt 1
plot "tof_monitor1_1.txt" with lines
set term wxt 2
plot "tof_monitor2_1.txt" with lines