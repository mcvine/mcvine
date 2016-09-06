#!/usr/bin/env python
#
#


category = 'monitors'


from mcni.AbstractComponent import AbstractComponent
class DGSSXResPixel( AbstractComponent ):

    __doc__ = """DGS Single Crystal Resolution Pixel
    """
    simple_description = "DGS Single Crystal Resolution Pixel"
    full_description = __doc__


    def __init__(self, name, pressure, tof, radius, height):
        AbstractComponent.__init__(self, name)
        # engine
        from mccomposite import mccompositebp 
        from mccomponents import mccomponentsbp
        shape = mccompositebp.Cylinder(radius, height)
        self.engine = mccomponentsbp.DGSSXResPixel(tof, pressure, shape)
        return

    def process(self, neutrons):
        return self.engine.process( neutrons )

    pass # end of Source


# End of file 
