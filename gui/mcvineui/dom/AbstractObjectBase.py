# -*- Python -*-
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


from dsaw.db.WithID import WithID
from dsaw.db.GloballyReferrable import GloballyReferrable
class AbstractObjectBase(WithID, GloballyReferrable):

    import dsaw.db

    date = dsaw.db.date( name='date' )
    date.meta['tip'] = 'date of creation'

    pass # end of OwnedObject


# version
__id__ = "$Id$"

# End of file 
