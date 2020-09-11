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


category = 'monitors'

from .MultiMonitors import MultiMonitors as base


def beam_analyzer(name, monitors):
    '''create a beam analyzer component

    a beam analyzer componennt is a bunch of monitors, each
    of which examine some quantities of neutrons

    name: name of the beam analyzer
    monitors: a list of monitor
    monitor: a tuple of quantities that the monitor is measuring

    E.g.

      beam_analyzer("ba", [("x", "y"), ("tof",)])
    '''

    # the class
    class BeamAnalyzer(base):
        
        class Inventory(base.Inventory):
            
            from mcni.pyre_support import facility

            for m in monitors:
                cname = componentname(m)
                c = _component(m, cname)
                code = '%s = facility("%s" , default=c)' % (cname, cname)
                exec(code)
                continue
            
        def _configure(self):
            self.monitors = [
                getattr(self.inventory, componentname(m))
                for m in monitors
                ]
            super(BeamAnalyzer, self)._configure()
            return


        pass # end
    
    return BeamAnalyzer(name)


# function to compute component name from the measured quantities
# like mtof or mx_y
componentname = lambda m: 'm' + '_'.join([q for q in m])


def _Component(quantities, name):
    from .ndmonitor import ndmonitor
    base = ndmonitor(*quantities)
    class Component(base):

        def __defaults__(self):
            super(Component, self)._defaults()
            self.inventory.filename = '%s.h5' % name
            return
    return Component


def _component(quantities, name):
    C = _Component(quantities, name)
    return C(name)


# version
__id__ = "$Id: MultiMonitors.py 659 2010-10-24 18:20:07Z linjiao $"

# End of file 
