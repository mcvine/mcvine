#!/usr/local/bin/gnuplot -persist

# Script for Gnuplot

set terminal png
set output "result/tt.png"
plot "tt_plot.txt" with lines

set output "result/tc.png"
plot "tc_plot.txt" with lines

set output "result/tb.png"
plot "tb_plot.txt" with lines

set output "result/wt.png"
plot "wt_plot.txt" with lines

set output "result/wc.png"
plot "wc_plot.txt" with lines

set output "result/wb.png"
plot "wb_plot.txt" with lines

