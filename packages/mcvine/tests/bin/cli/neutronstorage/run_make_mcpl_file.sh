OUT=out.make-mcpl-file
rm -rf $OUT
mcrun -c make-mcpl-file.instr -n 10 -d $OUT