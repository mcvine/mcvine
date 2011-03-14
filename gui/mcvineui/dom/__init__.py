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


def createRecordWithID(table, id):
    r = table()
    r.id = id
    return r


def insertRecordWithID(table, id, db):
    r = createRecordWithID(table, id)
    db.insertRow(r)
    return r


def getAllTypes():
    "get all data object types"
    from neutroncomponent_types import getTypes
    component_types = getTypes()
    from InstrumentConfiguration import InstrumentConfiguration
    return [InstrumentConfiguration] + component_types


def mapAllTypes(orm):
    map(orm, getAllTypes())
    return


from _ import o2t as object2table


# version
__id__ = "$Id$"

# End of file 
