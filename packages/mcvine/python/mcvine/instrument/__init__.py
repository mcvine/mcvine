# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

def main():
    import __main__ as m
    import sys
    assert len(sys.argv)==3
    ncount, buffer_size = map(int, sys.argv[1:])
    instrument = m.instrument
    N_iter = (ncount-1)//buffer_size + 1
    return

# End of file 
