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


from pyre.components.Component import Component as base1
from mcni.AbstractComponent import AbstractComponent as base2

class AbstractComponent( base1, base2 ):

    
    simple_description = 'Please give a simple description of this comonent'
    full_description = 'Please give a full description of this component'


    def __init__(self, name, facility = 'neutron component'):
        base2.__init__(self, name)
        base1.__init__(self, name, facility)

        self._outputdir = None
        return


    pass # end of AbstractComponent


# version
__id__ = "$Id$"

# End of file 
