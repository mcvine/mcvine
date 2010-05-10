# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcni import component_suppliers

from mcni.pyre_support import component_suppliers as pyre_component_suppliers

# include components provided by mccomponents
# XXX: maybe should have a new module for just pyre_support
import mccomponents.pyre_support


try: 
    import mcstas2
except ImportError:
    import warnings
    warnings.warn('mcstas2 not available')
else:
    component_suppliers.register(
        'mcstas2', component_suppliers.PyModuleAsSupplier('mcstas2'))
    pyre_component_suppliers.register(
        'mcstas2', pyre_component_suppliers.PyModuleAsSupplier('mcstas2.pyre_support'))


# version
__id__ = "$Id$"

# End of file 
