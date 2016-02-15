# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
mcvine: Monte Carlo VIrtual Neutron Experiment

Example 1: run a simple simulation

  >>> import mcvine
  >>> i = mcvine.instrument() # created an instrument
  >>> g = mcvine.geometer()   # created a geometer
  >>> f = mcvine.componentfactory('sources', 'Source_simple', 'mcstas2') # get a component factory
  >>> help(f)
  >>> s = f()  # instantiate a Source_simple component
  >>> i.append(s) # add the component to the instrument
  >>> g.register(s, (0,0,0), (0,0,0))  # register the new component with the geometer
  >>> neutrons = mcvine.neutron_buffer(5) # created a neutron buffer of size 5
  >>> print neutrons  
  >>> mcvine.simulate(i, g, neutrons)  # run the simulation
  >>> print neutrons

Example 2: find out the types of components in 'sources' category

  >>> import mcvine
  >>> mcvine.listallcomponentcategories()
  >>> mcvine.listcomponentsincategory('sources')

"""


import yaml, os
conf_path = "mcvine.conf"
config = dict()
if os.path.exists(conf_path):
    config = yaml.load(open(conf_path))

import logging.config
logging_conf = config.get("logging")
if logging_conf:
    logging.config.dictConfig(logging_conf)


# ----------------------------------------------------------------------
# create a convenient instance for handling units
# so that users can do:
# >>> from mcvine import units
# >>> units.meter
class _units(object):

    def __getattr__(self, key):
        from mcni.units import parser_singleton as parser
        return parser.parse(key)

    
    def parse(self, s):
        from mcni.units import parser_singleton as parser
        return parser.parse(s)


units = _units()
# done with units here
# ----------------------------------------------------------------------


from mcni import simulate, geometer, instrument, neutron_buffer, neutron, \
    componentfactory, findcomponentfactory, \
    listallcomponentcategories, listcomponentsincategory


def componentinfo(type, category=None, supplier=None):
    from mcni._find_component import find
    type, category, supplier = find(type, category=category, supplier=supplier)
    from mcni import componentinfo
    return  componentinfo(type=type, category=category, supplier=supplier)


import component_suppliers



__all__ = [
    'simulate', 'geometer', 'instrument', 'neutron_buffer', 'neutron',
    'componentinfo', 'componentfactory',
    'listallcomponentcategories', 'listcomponentsincategory',
    ]


# version
__id__ = "$Id$"

# End of file 
