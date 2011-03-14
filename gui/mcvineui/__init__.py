# -*- Python -*-
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


def createDefaultInstrumentConfiguration():

    from mcvineui.dom.InstrumentConfiguration import InstrumentConfiguration
    ic = InstrumentConfiguration()
    
    from mcvineui.dom.neutron_components.Source_simple import Source_simple
    source = Source_simple(); source.componentname = 'source'
    
    from mcvineui.dom.neutron_components.E_monitor import E_monitor
    monitor = E_monitor(); monitor.componentname = 'monitor'
    
    ic.components = [source, monitor]

    return ic


# version
__id__ = "$Id$"

# End of file 
