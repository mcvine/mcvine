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

def classes():
    '''return all binding classes'''
    import BoostPythonBinding
    return {'BoostPythonBinding': BoostPythonBinding.BoostPythonBinding}


def registries():
    import BoostPythonBinding 
    return { 'BoostPythonBinding': BoostPythonBinding.register }


def register( methodname, handlers, override = False ):
    regs = registries()
    for bindingname, handler in handlers.iteritems():
        regs[ bindingname ]( methodname, handler, override = override )
        continue
    return


# version
__id__ = "$Id$"

# End of file 
