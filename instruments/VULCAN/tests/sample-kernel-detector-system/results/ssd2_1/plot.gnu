#!/usr/bin/env gnuplot -persist


set terminal png
set xrange [800:1000]
set output "tof_monitor2_1.png"
plot "tof_monitor2_1.txt" with lines