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



from luban.content import select, alert, load


def select_one(id, ids):
    """
    returns actions that mark only one item as 'selected',
    and remove 'selected' Class from all others.

    id: id of the item to select
    ids: ids of all items
    """
    if id not in ids: raise RuntimeError
    actions = []
    for id1 in ids:
        if id1 != id:
            action = select(id=id1).removeClass('selected')
        else:
            action = select(id=id1).addClass('selected')
        actions.append(action)
        continue

    return actions



# version
__id__ = "$Id$"

# End of file 
