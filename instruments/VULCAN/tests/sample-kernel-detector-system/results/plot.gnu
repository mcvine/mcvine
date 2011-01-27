#!/usr/bin/env gnuplot -persist

set xrange [45:75]
set terminal png
set output "ssd1_2/e_monitor1_2.png"
plot "ssd1_2/e_monitor1_2.txt" with lines

set xrange [800:1000]
set output "ssd1_1/tof_monitor1_1.png"
plot "ssd1_1/tof_monitor1_1.txt" with lines
set output "ssd2_1/tof_monitor2_1.png"
plot "ssd2_1/tof_monitor2_1.txt" with lines