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

    def __init__(self, name, neutron, dx=0, dy=0):
        AbstractComponent.__init__(self, name)
        self.neutron = neutron
        if not dx and not dy:
            self.process = self._process_0
        else:
            self.dx = dx
            self.dy = dy
            self.process = self._process
        return


    def _process(self, neutrons):
        neutron = self.neutron
        N = len(neutrons)
        neutrons.clear()
        neutrons.resize(N, neutron)
        arr = neutrons.to_npyarr()
        
        # randomly distribute neutron position in x-y plane
        import numpy
        random_x = (numpy.random.random(N)-0.5) * self.dx
        random_y = (numpy.random.random(N)-0.5) * self.dy
        arr[:, 0] += random_x
        arr[:, 1] += random_y
        
        neutrons.from_npyarr(arr)
        return neutrons
    

    def _process_0(self, neutrons):
        neutron = self.neutron
        for i in range(len(neutrons)): neutrons[i] = neutron
        return neutrons


    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
