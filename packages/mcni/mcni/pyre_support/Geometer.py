#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from pyre.inventory.Property import Property

class Register(Property):


    def __init__(self, name, default=None, meta=None, validator=None):
        if default is None:
            default = default_record
            
        Property.__init__(self, name, "geometer-record", default, meta, validator)
        return


    def _cast(self, value):
        if isinstance(value, basestring):
            value = eval(value)
            pass
        
        if not isinstance(value, tuple) and not isinstance(value, list): invalid = True
        elif len(value) != 2: invalid = True
        elif len(value[0]) != 3 or len(value[1]) !=3: invalid = True
        else: invalid = False

        if invalid:
            raise ValueError , "%s. Good example: (0,0,3), (0,0,90)" % (
                value, )
        
        return value



default_record = (0,0,0), (0,0,0)



from mcni.Geometer import Geometer as base
from pyre.components.Component import Component

class Geometer(Component, base):


    def __init__(self, name = 'geometer'):
        Component.__init__(self, name, 'geometer')
        base.__init__(self)

        import journal
        self._warning = journal.warning( 'mcni.pyre_support.geometer' )
        return


    def position(self, element):
        try:
            return base.position( self, element )
        except:
            return base.position( self, element.name )


    def orientation(self, element):
        try:
            return base.orientation( self, element )
        except:
            return base.orientation( self, element.name )


    def _configure(self):
        Component._configure(self)
        for prop in self.inventory.propertyNames():
            v = self.inventory.getTrait( prop )
            if isinstance( v, Register ):
                position, orientation = self.inventory.getTraitValue( prop )
                self.register( prop, position, orientation )
                pass
            continue
        return


    pass # end of Geometer


def test():
    class G(Geometer):
        class Inventory(Geometer.Inventory):
            a = Register('a')
            pass
        pass
    g = G()
    g._configure()
    g._init()
    print g.position( 'a' ), g.orientation( 'a' )
    return

if __name__ == '__main__': test()

# version
__id__ = "$Id: Channel.py,v 1.1.1.1 2005/03/08 16:13:53 aivazis Exp $"

# End of file 
