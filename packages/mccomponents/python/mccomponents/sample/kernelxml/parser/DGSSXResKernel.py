#!/usr/bin/env python
#


from .KernelNode import KernelNode as base


class DGSSXResKernel(base):


    tag = "DGSSXResKernel"

    def createKernel( self, **kwds ):
        target_position = self._parse( kwds['target-position'] )
        target_radius = self._parse( kwds['target-radius'] )
        tof_at_target = self._parse( kwds['tof-at-target'] )
        dtof = self._parse( kwds['dtof'] )
        
        from mccomponents.sample import dgssxreskernel
        return dgssxreskernel(
            target_position, target_radius, tof_at_target, dtof)


    pass # end of DGSSXResKernel


# End of file 
