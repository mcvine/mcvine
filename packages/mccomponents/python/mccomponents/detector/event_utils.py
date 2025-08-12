#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import numpy as np

# please refer to EventModeMCA in libmccomponents/detector/
# for the struct definition for event
# { uint, uint, double }
datatype = np.dtype(
    [('pixelID',np.uint32), 
     ('tofChannelNo', np.uint32), 
     ('p', np.double),
     ])


def readEvents(file):
    events = np.fromfile(file, datatype)
    return events


def normalizeEventFile(file, n):
    "normalize the event data file by the number n"
    events = readEvents(file)
    events['p'] /= n
    return events.tofile(file)


def mergeEventFiles(files, out):
    "merge event data files into one output file"
    import sys, os
    if not sys.platform.startswith('linux'):
        raise NotImplementedError
    outdir = os.path.dirname(out)
    # tempfile to hold the list of files
    filelist = os.path.join(outdir, 'eventfiles-to-merge.list')
    with open(filelist, 'wt') as ostream:
        for f in files: ostream.write("%s\n" % f)
    cmd = 'cat %s | xargs -0 -d "\n" cat > "%s"' % (filelist, out)
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)
    return


# version
__id__ = "$Id: __init__.py 856 2011-02-09 16:52:39Z linjiao $"

# End of file 
