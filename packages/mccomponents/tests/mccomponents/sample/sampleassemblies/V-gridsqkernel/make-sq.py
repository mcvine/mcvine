import numpy as np
import histogram as H, histogram.hdf as hh

Q = np.arange(0, 12, 0.1)
sq = H.histogram(
    'S(Q)',
    [H.axis('Q', centers=Q)],
)
sq.I[:] = Q/10 + 1
hh.dump(sq, 'sq.h5')
