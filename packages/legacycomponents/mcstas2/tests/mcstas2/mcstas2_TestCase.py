#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# skip = True
standalone = True
is_interactive = False


import unittestX as unittest
import journal

import mcstas2

class TestCase(unittest.TestCase):

    def test1(self):
        'printcomponentinfo'
        mcstas2.printcomponentinfo( 'monitors', 'E_monitor' )
        return

    
    def test2(self):
        'list component categories'
        print mcstas2.listallcomponentcategories( )
        return


    def test3(self):
        'list components of a category'
        print mcstas2.listcomponentsincategory( 'monitors' )
        return


    def test4(self):
        'wrapcomponent'
        componentname = 'E_monitor'
        componentfile = '%s.comp' % componentname
        category = 'monitors'
        mcstas2.wrapcomponent( componentfile, category )
        from mcstas2.components import componentfactory
        emonfac = componentfactory( category, componentname )
        emon = emonfac(
            'emon',
            nchan=20, filename="e.dat",
            xmin=-0.2, xmax=0.2,
            ymin=-0.2, ymax=0.2,
            Emin=50., Emax=60.)
        if is_interactive:
            help( emonfac )
        return
    
    pass  # end of TestCase


if __name__ == "__main__":
    global is_interactive
    is_interactive = True
    unittest.main()
    
# End of file 
