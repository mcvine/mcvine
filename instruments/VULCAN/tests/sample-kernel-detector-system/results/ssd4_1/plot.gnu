#!/usr/local/bin/gnuplot -persist

# Script for Gnuplot

set terminal png
set output "tt.png"
plot "tt_plot.txt" with lines

set output "tc.png"
plot "tc_plot.txt" with lines

set output "tb.png"
plot "tb_plot.txt" with lines

set output "wt.png"
plot "wt_plot.txt" with lines

set output "wc.png"
plot "wc_plot.txt" with lines

set output "wb.png"
plot "wb_plot.txt" with lines

