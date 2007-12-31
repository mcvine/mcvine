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

def registries():
    import BoostPythonBinding 
    return { 'BoostPythonBinding': BoostPythonBinding.register }


def register( methodname, handlers ):
    regs = registries()
    for bindingname, handler in handlers.iteritems():
        regs[ bindingname ]( methodname, handler )
        continue
    return


# version
__id__ = "$Id$"

# End of file 
