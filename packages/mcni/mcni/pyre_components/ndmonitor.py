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

# quantity to expression translation
# required that evaluation environment has
#   x, y, z, vx, vy, vz, t  -- those quantities in the neutron event
#   mcni.utils.conversion as conversion
q2e = {
    'energy': 'conversion.VS2E * (vx*vx + vy*vy + vz*vz)',
    'divx': 'vx/vz',
    'divy': 'vy/vz',
    'tof': 't',
    }


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
    


def ndmonitor(*quantities, **kwds):
    '''
    ndmonitor("x", "vy")
    ndmonitor("x", "inverseX", inverseX="1/x")
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
            if not self._showHelpOnly and not self._noinit:
                self._saveFinalResult()
                
            super(Monitor, self)._fini()
            return
        
        
        def _init(self):
            super(Monitor, self)._init()
            if self._showHelpOnly or self._noinit:
                return
            
            if kwds:
                quantity2expression = q2e.copy()
                quantity2expression.update(kwds)
            else:
                quantity2expression = q2e
                
            NDMonitorBase._init(self)
            axes = []
            for q in quantities:
                if q not in neqs:
                    expr = quantity2expression[q]
                else:
                    expr = q
                n = getattr(self.inventory, 'n%s' % q)
                range = getattr(self.inventory, '%smin' % q),\
                        getattr(self.inventory, '%smax' % q)
                axis = q, expr, n, range
                axes.append(axis)
                continue

            self._engine_args = hname, axes
            self._createEngine()
            return

        
        def _createEngine(self):
            from ..components.NDMonitor import NDMonitor
            args = self._engine_args
            self.engine = NDMonitor(*args)
            return

        pass
    
    return Monitor


# function to compute histogram name from the measured quantities
# like itof or ix_y
histogramname = lambda m: 'i' + '_'.join([q for q in m])


# version
__id__ = "$Id: __init__.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
