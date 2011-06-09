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
    the neutron. Neutrons generated can come from a rectangular
    area whose size is determined by dx and dy, or can come from 
    just a single point in the space.
    '''

    __doc__ = simple_description + '\n' + full_description

    def __init__(self, name, neutron, dx=0, dy=0, dE=0):
        AbstractComponent.__init__(self, name)
        self.neutron = neutron
        self.dx = dx
        self.dy = dy
        self.dE = dE
        if not dx and not dy and not dE:
            self.process = self._process_0
        elif not dE:
            self.process = self._process_area
        else:
            self.process = self._process
        return


    # the process method in case neutrons coming from an area
    # and have an energy spread
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

        # gaussian distribution of neutron energy
        from ..utils.conversion import v2e
        E0 = self.neutron.energy()
        # .. energy samples
        samples = numpy.random.normal(loc=E0, scale=self.dE, size=N)
        # .. convert to velocities
        from numpy import sqrt
        scale_factors = sqrt(samples/E0) # velocity is prop to sqrt of E
        arr[:, 3] *= scale_factors
        arr[:, 4] *= scale_factors
        arr[:, 5] *= scale_factors        
        
        # back from array to neutrons
        neutrons.from_npyarr(arr)
        return neutrons
    

    # the process method in case neutrons coming from an area
    # but without energy spread
    def _process_area(self, neutrons):
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
    

    # the process method where all neutrons are exactly identical
    def _process_0(self, neutrons):
        neutron = self.neutron
        for i in range(len(neutrons)): neutrons[i] = neutron
        return neutrons


    pass # end of MonochromaticSource


# version
__id__ = "$Id$"

# End of file 
