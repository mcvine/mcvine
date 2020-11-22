#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

class HKL:

    hkl = ()                      # miller indexes
    F_squared = 0                 # |F|^2. units: barn

    def __init__(self, **kwds):
        for k, v in kwds.items():
            setattr(self, k, v)
            continue
        return


    def __repr__(self):
        return "HKL(hkl=%s, F_squared=%s)" % (
            self.hkl, self.F_squared)


# End of file
