# Test of E_Q_kernel

The tests here make sure that the S(Q) expression set in the E_Q_kernel
does translate to "measured" intensities following the S(Q) trend.

The E_Q_kernel_TestCase.TestCase.test1 check the float S(Q) case
which makes use of the kernel in subfolder "flat-S_Q".
This test makes use of the "ssm" application.

The subfolder "magnetic-form-factor" is an example inspired
by Gabriele Sala's research.
To run that example use the following command:

    $ ./ssm --ncount=1e6 --mpirun.nodes=20 --sample.xml=magnetic-form-factor/sampleassembly.xml
