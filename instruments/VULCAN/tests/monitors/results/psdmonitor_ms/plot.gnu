#!/usr/local/bin/gnuplot -persist

# Script for Gnuplot

set terminal png

set output "tc.png"
plot "tc_plot.txt" with lines

set output "wc.png"
plot "wc_plot.txt" with lines

