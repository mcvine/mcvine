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
except OSError:
    import warnings
    warnings.warn('mcstas2 not available due to OSError')
else:
    component_suppliers.register(
        'mcstas2', component_suppliers.PyModuleAsSupplier('mcstas2'))
    pyre_component_suppliers.register(
        'mcstas2', pyre_component_suppliers.PyModuleAsSupplier('mcstas2.pyre_support'))

"""
try: 
    import vitess
except ImportError:
    import warnings
    warnings.warn('vitess not available')
else:
    component_suppliers.register(
        'vitess', component_suppliers.PyModuleAsSupplier('vitess.components'))
    pyre_component_suppliers.register(
        'vitess', pyre_component_suppliers.PyModuleAsSupplier('vitess.pyre_components'))
"""

# End of file 
