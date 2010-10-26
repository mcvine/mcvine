#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')


import mccomponents.sample.diffraction.xml

def main():
    from mcvine.applications.InstrumentBuilder import build
    components = ['source', 'sample', 'detector']
    App = build(components)
    app = App('vulcan-ssd')
    app.run()
    return

if __name__ == '__main__': main()

# version
# $Id$


