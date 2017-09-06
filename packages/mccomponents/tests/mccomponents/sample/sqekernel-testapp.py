#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from mcvine.applications.InstrumentBuilder import build
components = ['source', 'sample', 'monitor']
App = build(components)
name = "sqekernel-test"

if __name__ == '__main__': App(name).run()
    
# End of file 
