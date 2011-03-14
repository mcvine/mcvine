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



class InstrumentConfiguration(object):

    components = []
    


from AbstractNeutronComponent import AbstractNeutronComponent
from neutroncomponent_types import getTypes
neutroncomponent_types = getTypes()


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    components = InvBase.d.referenceSet(
        name = 'components',
        targettype=AbstractNeutronComponent, targettypes=neutroncomponent_types,
        owned = 1)

    dbtablename = 'instrumentconfigurations'
    


InstrumentConfiguration.Inventory = Inventory
del Inventory


from _ import o2t
InstrumentConfigurationTable = o2t(InstrumentConfiguration)


## obsolete
## the instrument for which this configuration is about
## target = dsaw.db.reference(name='target', table=Instrument)
## componentsequence = dsaw.db.varcharArray(
##     name = 'componentsequence', length = 128, default = [] )
## components = vnf.dom.referenceSet(name='components')
## geometer = vnf.dom.geometer()
## configured = dsaw.db.boolean(name='configured', default=False)




# version
__id__ = "$Id$"

# End of file 
