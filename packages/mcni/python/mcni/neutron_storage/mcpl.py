try:
    import mcpl
except ImportError:
    raise RuntimeError("Failed to import mcpl. Please install mcpl python package.")
import os
import numpy as np

def mcpl2mcv(path, out, scale_by_number_of_packets):
    from ..utils import conversion
    from .idf_usenumpy import write
    # main loop
    myfile = mcpl.MCPLFile(path)
    base, ext = os.path.splitext(out)
    arrays = []
    for i,pb in enumerate(myfile.particle_blocks):
        x,y,z = pb.x/100., pb.y/100., pb.z/100.
        N1 = x.size
        t = pb.time/1e3
        p = pb.weight
        E = pb.ekin*1e9
        v = conversion.e2v(E)
        vv = v[:, np.newaxis] * pb.direction
        vx,vy,vz = vv.T
        # use spherical coordinates for spin: s1=theta, s2=phi
        sx,sy,sz = pb.polx, pb.poly, pb.polz
        ss = sx*sx + sy*sy + sz*sz
        s1 = np.arccos(sy/np.sqrt(ss))
        s2 = np.arctan2(sx,sz) # in radiant (phi)
        mask = ss<=0
        s1[mask] = 0
        s2[mask] = 0
        arr = np.array([x,y,z,vx,vy,vz,s1,s2,t,p]).T.copy()
        arrays.append(arr)
        # fn = '{}-{}{}'.format(base, i, ext)
        continue
    arr = np.concatenate(arrays); del arrays
    print("Read neutron data from ", path, " shape: ", arr.shape)
    assert len(arr.shape)==2 and arr.shape[-1]==10
    if scale_by_number_of_packets:
        N = arr.shape[0]
        arr[:, -1] *= N
    write(arr, out)
    return

def mcv2mcpl(mcvfile, mcplfile):
    from . import load
    neutrons = load(mcvfile)
    from mcni import mcnibp
    mcnibp.neutrons2mcpl(neutrons, mcplfile)
    return
