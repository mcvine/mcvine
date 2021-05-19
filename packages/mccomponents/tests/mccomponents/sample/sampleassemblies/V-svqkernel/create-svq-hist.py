import os, numpy as np
import histogram as H, histogram.hdf as hh

Qxaxis = H.axis('Qx', np.arange(-10, 10, 1.), '1/angstrom')
Qyaxis = H.axis('Qy', np.arange(-10, 11, 1.), '1/angstrom')
Qzaxis = H.axis('Qz', np.arange(-10, 12, 1.), '1/angstrom')
f = lambda x,y,z: np.abs(x+y*y+z*z*z)+1
h = H.histogram('I(Qx,Qy,Qz)', (Qxaxis, Qyaxis, Qzaxis), fromfunction=f)
hh.dump(h, 'svq.h5')
