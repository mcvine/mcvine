# -*- Python -*-
# 
# Jiao Lin <jiao.lin@gmail.com>
#


'''
factory to create an instrumnt pyre application class
from a list of component names.
'''

import os, sys, shutil

DEBUG_INSTRUMENT_APP_PROXY = os.environ.get('DEBUG_INSTRUMENT_APP_PROXY')

def build(neutron_components):
    
    class _Proxy:
        """proxy class of instrument sim app"""
        
        def __init__(self, *args, **kwds):
            self._init_params = args, kwds
            return

        def run(self, *args, **kwds):
            # create a temp work dir
            import tempfile
            workdir = tempfile.mkdtemp()
            # create an application script
            apppath = os.path.join(workdir, 'simapp.py')
            appscript = """from mcvine.applications.InstrumentBuilder import _build
components = ['source', 'sample', 'storage']
App = _build(%(neutron_components)r)
args, kwds = %(init_params)r
app = App(*args, **kwds)
args, kwds = %(run_params)r
app.run()
""" % dict(neutron_components=neutron_components, 
           init_params = self._init_params,
           run_params = (args, kwds))
            open(apppath, 'wt').write(appscript)
            # run the script in a subprocess
            sysargs = ' '.join('"%s"' % a for a in sys.argv[1:])
            cmd = '%s %s %s' % (sys.executable, apppath, sysargs)
            print "* Running %s" % cmd
            if os.system(cmd):
                raise RuntimeError("%s failed" % cmd)
            # clean up
            if not DEBUG_INSTRUMENT_APP_PROXY:
                shutil.rmtree(workdir)
            return
    _Proxy.neutron_components = neutron_components
    return _Proxy


def _build(neutron_components):
    
    from mcni.pyre_support.Instrument import Instrument as base
    class Instrument(base):

        class Inventory( base.Inventory ):

            from mcni.pyre_support import facility, componentfactory as component
            import mccomponents.pyre_support

            for name in neutron_components:
                code = '%s = facility("%s", default="mcni://optics/Dummy" )' % (
                    name, name)
                exec code in locals()
                continue
            del code, name

            import pyre.inventory as pinv
            # path of the post processing script
            # the components that need post-processing should append
            # to this script
            post_processing_script = pinv.str("post-processing-script")

            pass # end of Inventory


        def _defaults(self):
            base._defaults(self)
            self.inventory.sequence = neutron_components
            pps = self.inventory.post_processing_script
            if not pps:
                pps = os.path.join(self.inventory.outputdir, 'post-processing-script.py')
            self.post_processing_script = pps
            return


        def _makeSimContext(self):
            context = base._makeSimContext(self)
            context.post_processing_script = self.post_processing_script
            return context

        pass # end of Instrument

    return Instrument


# End of file 
