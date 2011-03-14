# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class AbstractNeutronComponent(object):
    
    abstract = True

    componentname = 'name'
    # position = [0.,0.,0.]
    # orientation = [[1.,0.,0.],
    #               [0.,1.,0.],
    #               [0.,0.,1.],]
    # referencename = ''

    # short_description = ''

    def customizeLubanObjectDrawer(self, drawer):
        drawer.mold.sequence = ['componentname']


    pass # end of AbstractNeutronComponent


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    componentname = InvBase.d.str(
        name='componentname', default='name', validator = InvBase.v.variablename)
    componentname.label = 'name'
    componentname.help = 'name of the component'

    # position = InvBase.d.array(
    #    name='position',
    #    elementtype='float',
    #    shape=3,
    #    default=AbstractNeutronComponent.position,
    #    )
    # position.help = 'position of this component relative to the reference component'

    # orientation = InvBase.d.array(
    #    name='orientation',
    #    elementtype='float',
    #    shape=(3,3),
    #    default = AbstractNeutronComponent.orientation,
    #    )
    # orientation.help = 'orientation of this component relative to the reference component'

    # referencename = InvBase.d.str(name='referencename')
    # referencename.label = 'reference'
    # referencename.help = 'name of the component as reference. if blank, position and orientation are absolute'

    # short_description = InvBase.d.str(name='short_description')
    # short_description.label = 'description (optional)'
    # short_description.help = 'Give a brief description of this component'


AbstractNeutronComponent.Inventory = Inventory
del Inventory


# version
__id__ = "$Id$"

# End of file 
