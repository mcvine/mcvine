#!/usr/bin/env python
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')

def main():
    from mcvine.applications.InstrumentBuilder import build
    components = ['source', 'sample', 'storage']
    App = build(components)
    app = App('sss')
    app.run()
    return

if __name__ == '__main__': main()
