from ...AbstractComponent import AbstractComponent
from mcni.components.ParallelComponent import ParallelComponent

class Component(AbstractComponent, ParallelComponent):

    def __init__(self, cpp_instance_factory, *args, **kwds):
        # args, if exists, must be "name"
        assert len(args) in [0, 1]
        # get user inputs
        if args: kwds['name' ] = args[0]
        for k, v in kwds.items():
            setattr(self, k, v)
        # get defaults
        all = dict()
        iparams = cpp_instance_factory.info.input_parameters
        for p in iparams: all[p.name] = p.default
        # combine
        all.update(kwds)
        # store
        self._factory_kwds = all
        self.restore_neutron = False
        self._cpp_instance_factory = cpp_instance_factory
        self.__cpp_instance = None
        return

    # lazy creation of the cpp instance
    @property
    def _cpp_instance(self):
        if self.__cpp_instance is None:
            # self.__cpp_instance is an instance created
            # by factory methods auto-generated from mcstas components
            # see template code in mcstas2.wrappers.pymodule.factorymethod_py
            self.__cpp_instance = self._cpp_instance_factory(**self._factory_kwds)
        return self.__cpp_instance

    # allow change attributes after construction, but before self._cpp_instance is accessed
    def __setattr__(self, name, value):
        if hasattr(self, "_factory_kwds") and name in self._factory_kwds:
            self._factory_kwds[name] = value
            return value
        return object.__setattr__(self, name, value)

    def __getattr__(self, name):
        if name in self._factory_kwds:
            return self._factory_kwds[name]
        raise AttributeError(name)

    def process(self, neutrons):
        self.__cpp_instance = None # clean up
        restore_neutron = self.restore_neutron
        if restore_neutron:
            # create a copy to be processed
            saved = neutrons.snapshot(len(neutrons))
        # and process neutrons as normal
        ret = self._cpp_instance.process(neutrons)
        # dump all calculated data
        self._dumpData()
        # restore neutrons if requested
        if restore_neutron:
            neutrons.swap(saved)
        return ret

    def get_display(self):
        "obtain a list of display instructions"
        # this is done by running the mcstas display function in a subprocess.
        # and obtain the output. mcstas display function always prints to stdout.
        # after getting the output, parse it and only retain the display instructions
        # 1. temp file to save the constructor information for the C++ component
        import os, tempfile
        tmpdir = tempfile.mkdtemp()
        path = os.path.join(tmpdir, 'ctor.pkl')
        import pickle
        pickle.dump((self._cpp_instance_factory, self._factory_kwds), open(path, 'w'))
        # 2. run python cmd in subprocess that calls mcstas display function
        cmd = 'python -m "mcstas2.components._proxies.base" display --path="%s"' % path
        import subprocess as sp, shlex
        out = sp.check_output(shlex.split(cmd))
        # 3. parse output
        prefix = 'MCDISPLAY: '
        return [l.lstrip(prefix) for l in out.splitlines() if l.startswith(prefix)]

    def _display(self):
        "call the mcstas C code for display. this will prints to stdout"
        self._cpp_instance.core().display()
        return

    def _dumpData(self):
        return

import click
@click.command()
@click.argument("action")
@click.option("--path", help="path to display")
def main(action, path):
    assert action == 'display'
    # load constructor info for the component
    import pickle
    f, kwds = pickle.load(open(path))
    # create component instance
    instance = f(**kwds)
    # call display method
    instance.core().display()
    return

if __name__ == '__main__': main()

# End of file 
