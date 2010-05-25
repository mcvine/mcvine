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


category = 'sources'


from mcni.AbstractComponent import AbstractComponent

class MonochromaticSource( AbstractComponent ):

    simple_description = 'Monochromatic neutron source'

    full_description = '''
    This monochromatic neutron source, altough unreal, is very useful
    in testing your simulation. It generates a neutron beam that consists
    of only one kind of neutron of your choice. You will need to
    specify the speed, position, time-of-flight, and probability of
    the neutron.
    '''

    __doc__ = simple_description + '\n' + full_description

    def __init__(self, name, neutron):
        AbstractComponent.__init__(self, name)
        self.neutron = neutron
        return


    def process(self, neutrons):
        neutron = self.neutron
        for i in range(len(neutrons)): neutrons[i] = neutron
        return neutrons


    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
