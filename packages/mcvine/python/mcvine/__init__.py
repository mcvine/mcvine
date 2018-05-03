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
  >>> i = mcvine.instrument()
  >>> # add source
  >>> i.append(mcvine.components.sources.Source_simple('source'), position=(0,0,0))
  >>> # add monitor
  >>> i.append(mcvine.components.monitors.E_monitor('monitor', filename='IE.dat'), position=(0,0,1))
  >>> # simulate
  >>> neutrons = i.simulate(5,outputdir="out-mcvine", overwrite_datafiles=True, iteration_no=0)
  >>> print neutrons

Example 2: find out the types of components in 'sources' category

  >>> import mcvine
  >>> mcvine.listallcomponentcategories()
  >>> mcvine.listcomponentsincategory('sources')

"""

from .version import version, git_revision

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
components = component_suppliers.components
del component_suppliers.components

__all__ = [
    'simulate', 'geometer', 'instrument', 'neutron_buffer', 'neutron',
    'componentinfo', 'componentfactory',
    'listallcomponentcategories', 'listcomponentsincategory',
    ]


# End of file 
