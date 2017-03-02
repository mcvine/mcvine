#!/usr/bin/env python
#
#   Jiao Lin
#

def populate_Ei_data(beam_outdir, nxs):
    import json, os
    props_path = os.path.join(beam_outdir, 'props.json')
    s = open(props_path).read()
    s = s.replace("'", '"') # ' -> "
    props = json.loads(s)
    Ei, unit = props['average energy'].split()
    Ei = float(Ei)
    assert unit == 'meV'
    setEnergyRequest(nxs, Ei)
    return


def setEnergyRequest(path, Ei):
    """set energy request value into an CNCS processed nexus file
    
    path: path of the nexus file
    Ei: unit meV
    
    caveat: the nexus template file should already have /???workspace???/logs/EnergyRequest which contains the appropriate sub-datasets with correct attributes.
    """
    import h5py
    f = h5py.File(path, 'a')
    # XXX assume the workspace is the first node at root XXX
    ws = f.values()[0]
    logs = ws['logs']
    er = logs['EnergyRequest']
    er['value'][0] = Ei
    f.close()
    return


# End of file 
