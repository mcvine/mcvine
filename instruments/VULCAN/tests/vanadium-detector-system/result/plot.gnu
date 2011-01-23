#!/usr/local/bin/gnuplot -persist

# Script for Gnuplot

set terminal png
set output "tt.png"
plot "tt.txt" with lines

set output "tc.png"
plot "tc.txt" with lines

set output "tb.png"
plot "tb.txt" with lines

set output "wt.png"
plot "wt.txt" with lines

set output "wc.png"
plot "wc.txt" with lines

set output "wb.png"
plot "wb.txt" with lines

