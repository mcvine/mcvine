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



class CompositeScatterer:
    

    def __init__(
        self, shape = None,
        max_multiplescattering_loops_among_scatterers = None,
        max_multiplescattering_loops_interactM_path1 = None,
        min_neutron_probability = None,
        ):
        from Geometer import Geometer
        self.geometer = Geometer()
        self._elements = []
        self._shape = shape
        self.setMultipleScatteringParams(
            max_multiplescattering_loops_interactM_path1 = \
                max_multiplescattering_loops_interactM_path1,
            max_multiplescattering_loops_among_scatterers = \
                max_multiplescattering_loops_among_scatterers,
            min_neutron_probability = min_neutron_probability,
            )
        return
    

    def setMultipleScatteringParams(
        self, 
        max_multiplescattering_loops_among_scatterers = None,
        max_multiplescattering_loops_interactM_path1 = None,
        min_neutron_probability = None,
        ):
        self.max_multiplescattering_loops_among_scatterers = max_multiplescattering_loops_among_scatterers or 5
        self.max_multiplescattering_loops_interactM_path1 = max_multiplescattering_loops_interactM_path1 or 1
        self.min_neutron_probability = min_neutron_probability or 0.
        return


    def addElement(self, element, position = (0,0,0), orientation = (0,0,0) ):
        self._elements.append(element)
        self.geometer.register(element, position, orientation)
        return


    def elements(self): return self._elements


    def identify(self, visitor): return visitor.onCompositeScatterer(self)


    def shape(self):
        if self._shape is None:
            from geometry.operations import unite
            self._shape = unite( *[self._getElementShape(e)
                                   for e in self.elements() ] )
            pass
        return self._shape


    def _getElementShape(self, e):
        s = e.shape()
        g = self.geometer
        position = g.position(e)
        orientation = g.orientation(e)
        import geometry
        r = geometry.operations.rotate(s, euler_angles=orientation)
        t = geometry.operations.translate(r, vector=position)
        return t
    

    pass # end of CompositeScatterer



# version
__id__ = "$Id$"


# End of file 
