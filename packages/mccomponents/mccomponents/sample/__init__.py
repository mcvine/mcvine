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


def gridsqe(*args, **kwds):
    from register_GridSQE import GridSQE
    return GridSQE( *args, **kwds )


def sqekernel(*args, **kwds):
    from register_SQEkernel import SQEkernel
    return SQEkernel( *args, **kwds )


# version
__id__ = "$Id$"

# End of file 
