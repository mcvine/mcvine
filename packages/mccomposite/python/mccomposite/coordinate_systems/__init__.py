#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

choices = [
    'McStas',  # z-downstream, y-vertical up
    'InstrumentScientist', # z-vertical up, x -downstream
    ]


def computationEngineRenderAdpator( coordinate_system = "McStas" ):
    klassname = "%sCSAdaptor_for_ShapeComputationEngineRenderer" % coordinate_system
    exec 'from %s import %s as klass' % (klassname, klassname)
    return klass


# version
__id__ = "$Id$"

# End of file 
