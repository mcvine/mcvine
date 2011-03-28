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
    print "read %s events" % len(events)
    print "events[0]= %s" % events[0]
    return events


def normalizeEventFile(file, n):
    "normalize the event data file by the number n"
    events = readEvents(file)
    events['p'] /= n
    return events.tofile(file)


def mergeEventFiles(files, out):
    "merge event data files into one output file"
    import sys, os
    if sys.platform != 'linux2':
        raise NotImplementedError
    cmd = ['cat'] 
    cmd += [ '"%s"' % f for f in files ]
    cmd.append( '> "%s"' % out)
    cmd = ' '.join(cmd)
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd
    return


# version
__id__ = "$Id: __init__.py 856 2011-02-09 16:52:39Z linjiao $"

# End of file 
