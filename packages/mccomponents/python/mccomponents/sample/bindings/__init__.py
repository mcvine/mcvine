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


from mccomponents.homogeneous_scatterer.bindings import default, get

def _import():
    try:
        from . import BoostPythonBinding
    except:
        import warnings, journal, traceback
        warnings.warn('binding not imported')
        journal.debug('BoostPythonBinding').log(traceback.format_exc())
    return

_import()


# version
__id__ = "$Id$"

# End of file 
