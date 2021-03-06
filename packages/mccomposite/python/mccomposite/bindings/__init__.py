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


def default( ): return get('BoostPython')


def get( type ):
    """retrieve binding of given type

    Example: get('BoostPython')
    """
    return classes()[ '%sBinding' % type ]( )


def classes():
    '''return all binding classes'''
    from . import BoostPythonBinding
    return {'BoostPythonBinding': BoostPythonBinding.BoostPythonBinding}


def registries():
    from . import BoostPythonBinding 
    return { 'BoostPythonBinding': BoostPythonBinding.register }


def register( methodname, handlers, override = False ):
    regs = registries()
    for bindingname, handler in handlers.items():
        regs[ bindingname ]( methodname, handler, override = override )
        continue
    return


# version
__id__ = "$Id$"

# End of file 
