#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                                  Jiao  Lin
#                        California Institute of Technology
#                        (C) 2006-2013  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

"""
This module provides a wrapper of pyre journal.
It allows developers to create logging that is fixed format
(not configurable by user). 
This is totally against the general idea of the design of journal,
so use it only when you really need that functionality.
Usually, journal formatting should be configurable from
command line, config files, etc, like normal pyre thing.
But in some cases, we do need to fix the formatting.
Right now it is used in 
* mcni.pyre_support.Instrument
* mcni.instrument_simulator.SimulationNode

"""

class journal(object):

    @classmethod
    def logger(cls, type, name, **kwds):
        return _journal_logger(type, name, **kwds)
        

class _journal_logger(object):
    
    def __init__(self, type, name, header=None, format=None, footer=None):
        self.type = type
        self.name = name
        self.header, self.format, self.footer = header, format, footer
        return

    
    def __call__(self, msg):
        import journal
        r = journal.journal().device.renderer
        header, footer, format = r.header, r.footer, r.format
        r.header, r.footer, r.format = self.header, self.footer, self.format
        getattr(journal, self.type)(self.name).log(msg) # journal.info('abc').log()
        r.header, r.footer, r.format = header, footer, format
        return

# version
__id__ = "$Id$"

#  End of file 
