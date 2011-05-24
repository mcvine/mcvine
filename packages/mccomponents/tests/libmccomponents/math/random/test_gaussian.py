#!/usr/bin/env python

def main():
    import os
    outf = 'out-test_gaussian'
    os.system('./test_gaussian > %s' % outf)
    y = open(outf).readlines()
    y = map(float, y)
    import numpy
    x = numpy.arange(-5, 5, 10./200)
    import pylab
    pylab.plot(x,y)
    pylab.show()
    return

if __name__ == '__main__': main()
