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
    
    from mcvineui.dom.neutron_components.Arm import Arm
    arm1 = Arm()
    arm2 = Arm()
    arm3 = Arm()
    
    ic.components = [arm1, arm2, arm3]

    return ic


# version
__id__ = "$Id$"

# End of file 
