# -*- python -*-
# 
# Jiao Lin <jiao.lin@gmail.com>
#


import numpy as np
def vitess2mcvine(vns):
    # output array
    from mcni.neutron_storage import ndblsperneutron
    arr = np.zeros((vns.size, ndblsperneutron))
    x = arr[:,0]; y = arr[:,1]; z = arr[:,2]
    vx = arr[:,3]; vy = arr[:,4]; vz = arr[:,5]
    s1 = arr[:,6]; s2 = arr[:,7];
    t = arr[:,8];
    p = arr[:,9]
    
    # cm -> m
    x[:] = 0.01*vns['Position'][:, 1]
    y[:] = 0.01*vns['Position'][:, 2]
    z[:] = 0.01*vns['Position'][:, 0]
    # speed
    lambda1 = vns['Wavelength']
    v = 3956.0346/lambda1; 
    vx[:] = v*vns['Vector'][:, 1]
    vy[:] = v*vns['Vector'][:, 2]
    vz[:] = v*vns['Vector'][:, 0]
    # XXX: ignore spin for now
    # micro second -> second
    t[:] = 0.001*vns['Time']
    #
    p[:] = vns['Probability']
    return arr


# End of file
