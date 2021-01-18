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
        
        Instrument = _build(neutron_components)
    
        def __init__(self, *args, **kwds):
            self._init_params = args, kwds
            return

        def run(self, *args, **kwds):
            # create a temp work dir
            import tempfile
            workdir = tempfile.mkdtemp(dir = os.path.abspath(os.curdir), prefix='simapp-')
            # create an application script
            apppath = os.path.join(workdir, 'simapp.py')
            appscript = """from mcvine.applications.InstrumentBuilder import _build
App = _build(%(neutron_components)r)
args, kwds = %(init_params)r
app = App(*args, **kwds)
args, kwds = %(run_params)r
app.run(*args, **kwds)
""" % dict(neutron_components=neutron_components, 
           init_params = self._init_params,
           run_params = (args, kwds))
            with open(apppath, 'wt') as ostream:
                ostream.write(appscript)
            # create run.sh
            sysargs = ' '.join('"%s"' % a for a in sys.argv[1:])
            ppsd = os.path.join(workdir, 'post-processing-scripts')
            sysargs += ' --post-processing-scripts-dir=%s' % ppsd
            logpath = os.path.join(workdir, 'log.sim')
            cmd = '%s %s %s\n' % (sys.executable, apppath, sysargs)
            run_sh_path = os.path.join(workdir, 'run.sh')
            with open(run_sh_path, 'wt') as ostream:
                ostream.write(cmd)
            # run run.sh
            if DEBUG_INSTRUMENT_APP_PROXY:
                print("* Logs are also saved at %s" % logpath)
            with open(logpath, 'w') as logstream:
                cmd = 'bash %s' % run_sh_path
                print(cmd)
                _exec(cmd, logstream)
            # run the postprocessing script
            from mcni import run_ppsd_in_parallel
            nodes = _get_nodes_option()
            run_ppsd_in_parallel(ppsd, nodes)
            # clean up
            if not DEBUG_INSTRUMENT_APP_PROXY:
                shutil.rmtree(workdir)
            return

    _Proxy.neutron_components = neutron_components
    return _Proxy


def _get_nodes_option():
    for a in sys.argv:
        if a.startswith('--') and '.nodes' in a:
            if DEBUG_INSTRUMENT_APP_PROXY:
                print("* nodes option: %r" % a)
            # --mpirun.nodes=10
            opt,v = a.split('=')
            assert opt.endswith('.nodes')
            return int(v)
    return 1
            

def _exec(cmd, logstream):
    if DEBUG_INSTRUMENT_APP_PROXY: 
        print("* Running %s" % cmd)
    #
    import subprocess as sp, shlex
    import psutil
    args = shlex.split(cmd)
    with psutil.Popen(args, stdout=sp.PIPE) as process:
        for line in iter(process.stdout.readline, b''):
            sys.stdout.write(line.decode())
            logstream.write(line.decode())
        process.wait()
        errcode = process.returncode
        # process.kill()
    if errcode:
        raise RuntimeError("%s failed" % cmd)
    return

def _build(neutron_components):
    
    from mcni.pyre_support.Instrument import Instrument as base
    class Instrument(base):

        class Inventory( base.Inventory ):

            from mcni.pyre_support import facility, componentfactory as component
            import mccomponents.pyre_support

            for name in neutron_components:
                code = '%s = facility("%s", default="mcni://optics/Dummy" )' % (
                    name, name)
                exec(code, locals())
                continue
            del code, name
            pass # end of Inventory

        def _defaults(self):
            base._defaults(self)
            self.inventory.sequence = neutron_components
            return

        pass # end of Instrument

    return Instrument


# End of file 
