#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



# quantities that are already in the neutron event record
neqs = [
    'x', 'y', 'z',
    'vx', 'vy', 'vz',
    't',
    ]


# quantity to be computed for the monitor
class Quantity:
    
    name = ''
    expression = ''
    unit = ''

    def __init__(self, **kwds):
        for k,v in kwds.iteritems():
            setattr(self, k, v)


# quantity to expression translation
# required that evaluation environment has
#   x, y, z, vx, vy, vz, t  -- those quantities in the neutron event
#   mcni.utils.conversion as conversion
#
# please note the unit are determined by the expression
# the expression are using constants in "conversion" module
# right now this conversion module is mcni.utils.conversion
# so read that module to find out the unit.
quantities = [
    Quantity(name='energy', 
             expression='conversion.VS2E * (vx*vx + vy*vy + vz*vz)',
             unit = 'meV'),
    # wavelength
    Quantity(name='w',
             expression = 'conversion.RV2W * 1/sqrt(vx*vx + vy*vy + vz*vz)', 
             unit = 'angstrom'),
    # wave vector
    Quantity(name='q',
             expression= 'conversion.V2K * sqrt(vx*vx + vy*vy + vz*vz)',
             unit = 'angstrom**-1'),
    Quantity(name='divx',
             expression = 'vx/vz',
             unit = 1),
    Quantity(name='divy',
             expression = 'vy/vz',
             unit = 1),
    Quantity(name='tof',
             expression = 't',
             unit = 'second'),
    Quantity(name='x',
             expression = 'x',
             unit = 'meter'),
    Quantity(name='y',
             expression = 'y',
             unit = 'meter'),
    Quantity(name='z',
             expression = 'z',
             unit = 'meter'),
    Quantity(name='vx',
             expression = 'vx',
             unit = 'meter/second'),
    Quantity(name='vy',
             expression = 'vy',
             unit = 'meter/second'),
    Quantity(name='vz',
             expression = 'vz',
             unit = 'meter/second'),
    Quantity(name='t',
             expression = 't',
             unit = 'second'),
    ]

# quantity to expression conversion
# quantity to unit conversion
q2e = {}; q2u = {}
for q in quantities:
    q2e[q.name] = q.expression
    q2u[q.name] = q.unit


from mcni.components.HistogramBasedMonitorMixin import HistogramBasedMonitorMixin
from mcni.pyre_support.ParallelComponent import ParallelComponent
from mcni.pyre_support.AbstractComponent import AbstractComponent
class NDMonitorBase(HistogramBasedMonitorMixin, ParallelComponent, AbstractComponent):
    supplier = 'mcni'
    category = 'monitors'
    type = 'NDMonitor'

    class Inventory(AbstractComponent.Inventory):
        
        import pyre.inventory
        
        filename = pyre.inventory.str('filename', default='')
        filename.meta['tip'] = "file name for output histogram"

        title = pyre.inventory.str('title', default='')
        title.meta['tip'] = 'Title of the histogram'

        xwidth = pyre.inventory.str('xwidth', default=0.1)
        xwidth.meta['tip'] = 'Width of the monitor'

        yheight = pyre.inventory.str('yheight', default=0.1)
        yheight.meta['tip'] = 'Height of the monitor'
    


def ndmonitor(*quantities, **kwds):
    '''
    ndmonitor("x", "vy")
    ndmonitor("x", "inverseX", inverseX="1/x")
    ndmonitor("x", "inverseX", inverseX="1/x", inverseX_unit='meter**-1')
    '''

    hname = histogramname(quantities)

    class Monitor(NDMonitorBase):

        simple_description = "Multidimensional monitor"
        if not len(quantities):
            full_description = (
                "You have not specified the quantities this monitor will measure. "
                "Please specify additional arguments for the quantities to measure. "
                "For example, NDMonitor(x,y) is a monitor of I(x,y) histogram. "
                )
        else:
            full_description = (
                "Monitor collecting histogram of I(%s). " % (', '.join(quantities))
                )

        class Inventory( NDMonitorBase.Inventory ):

            import pyre.inventory

            for q in quantities:

                name = q
                code = '%smin = pyre.inventory.float("%smin", default=0)' % (name, name)
                exec code
                code = '%smin.meta["tip"] = "minimum of %s"' % (name, name)
                exec code
                code = '%smax = pyre.inventory.float("%smax", default=1)' % (name, name)
                exec code
                code = '%smax.meta["tip"] = "maximum of %s"' % (name, name)
                exec code
                code = 'n%s = pyre.inventory.int("n%s", default=10)' % (name, name)
                exec code
                code = 'n%s.meta["tip"] = "number of bins for %s"' % (name, name)
                exec code
                
                continue
            

        def process(self, neutrons):
            ret = self.engine.process( neutrons )
            
            # 
            self._dumpData(self.simulation_context.getOutputDirInProgress())

            # recreate engine
            self._createEngine()
            
            return ret


        def _dumpData(self, dir):
            h = self.engine.histogram
            title = self.inventory.title
            h.setAttribute('title', title)

            from histogram.hdf import dump
            f = self._getHistogramFilename()
            import os
            f = os.path.join(dir, f)
            dump(h, f, '/', 'c')
            return

        
        # required by HistogramBasedMonitorMixin
        def _getHistogramFilename(self):
            return self.inventory.filename or \
                ('%s.h5' % hname)
        
        
        def _fini(self):
            if not self._showHelpOnly:
                self._saveFinalResult()
                
            super(Monitor, self)._fini()
            return
        
        
        def _init(self):
            super(Monitor, self)._init()
            if self._showHelpOnly:
                return
            
            if kwds:
                quantity2expression = q2e.copy()
                quantity2unit = q2u.copy()
                for k, v in kwds.iteritems():
                    if k.endswith('_unit'):
                        quantity2unit[k[:-5]] = v
                    else:
                        quantity2expression[k] = v
                
            else:
                quantity2expression = q2e
                quantity2unit = q2u
                
            NDMonitorBase._init(self)
            axes = []
            from ..components.NDMonitor import Axis
            for q in quantities:
                if q not in neqs:
                    expr = quantity2expression[q]
                else:
                    expr = q
                unit = quantity2unit[q]
                n = getattr(self.inventory, 'n%s' % q)
                range = getattr(self.inventory, '%smin' % q),\
                        getattr(self.inventory, '%smax' % q)
                axis = Axis(
                    name=q, expression=expr, 
                    bins=n, range=range,
                    unit = unit,
                    )
                axes.append(axis)
                continue

            xwidth  = float(self.inventory.xwidth)
            yheight = float(self.inventory.yheight)
            if xwidth <=0 or yheight <=0:
                raise Exception("Zero or negative area: xwidth=%s, yheight=%s",
                                (self.inventory.xwidth, self.inventory.yheight))

            size    = xwidth, yheight     # monitor size
            self._engine_args = hname, axes, size
            self._createEngine()
            return

        
        def _createEngine(self):
            from ..components.NDMonitor import NDMonitor
            args = self._engine_args
            self.engine = NDMonitor(*args)
            return

        pass

    Monitor.__name__ = "NDMonitor"
    
    return Monitor


# function to compute histogram name from the measured quantities
# like itof or ix_y
histogramname = lambda m: 'i' + '_'.join([q for q in m])


# version
__id__ = "$Id: __init__.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
