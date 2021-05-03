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
            kwds = self._factory_kwds
            key = 'restore_neutron'
            if key in kwds: del kwds[key]
            self.__cpp_instance = self._cpp_instance_factory(**kwds)
        return self.__cpp_instance

    # allow change attributes after construction, but before self._cpp_instance is accessed
    def __setattr__(self, name, value):
        if "_factory_kwds" in self.__dict__ and name in self._factory_kwds:
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

    def draw(self, painter):
        "draw this component using the painter"
        instructions = self.get_display_instructions()
        import ast
        for ins in instructions:
            f, args = ins.rstrip(')').split('(')
            assert not f.startswith('_')
            func = getattr(painter, f)
            args = ast.literal_eval(args)
            if not isinstance(args, tuple): args = args,
            func(getattr(_painting_action_translator, f)(*args))
        return

    def get_display_instructions(self):
        "obtain a list of display instructions"
        # this is done by running the mcstas display function in a subprocess.
        # and obtain the output. mcstas display function always prints to stdout.
        # after getting the output, parse it and only retain the display instructions
        # 1. temp file to save the constructor information for the C++ component
        import os, tempfile
        tmpdir = tempfile.mkdtemp()
        path = os.path.join(tmpdir, 'ctor.pkl')
        import pickle
        pickle.dump((self._cpp_instance_factory, self._factory_kwds), open(path, 'wb'))
        # 2. run python cmd in subprocess that calls mcstas display function
        cmd = 'python -m "mcstas2.components._proxies.base" display --path="%s"' % path
        import subprocess as sp, shlex
        out = sp.check_output(shlex.split(cmd))
        out = out.decode()
        # 3. parse output
        prefix = 'MCDISPLAY: '
        return [l.lstrip(prefix) for l in out.splitlines() if l.startswith(prefix)]

    def _call_mcstas_display(self):
        "call the mcstas C code for display. this will prints to stdout"
        self._cpp_instance.core().display()
        return

    def _dumpData(self):
        return

class _PaintingActionTranslation:

    def multiline(self, *x):
        import numpy as np
        N = x[0]
        x = np.array(x[1:])
        x.shape = -1, 3
        assert x.shape[0] == N
        return x

    def circle(self, plane, cx, cy, cz, r):
        c = cx,cy,cz
        return plane, c, r

    def magnify(self, plane):
        return plane
_painting_action_translator = _PaintingActionTranslation()


class AbstractPainter:

    def multiline(self, x):
        """draw lines between successive points

        Parameters
        ----------
        x : array
          numpy array of points. shape (N,3)
        """
        raise NotImplementedError("multiline")

    def circle(self, plane, c, r):
        """draw a circle

        Parameters
        ----------
        plane : string
          xy/yz/xz
        c : vector
          center. 3D vector.
        r : float
          radius
        """
        raise NotADirectoryError("circle")

    def magnify(self, plane):
        """magnify

        Parameters
        ----------
        plane : string
          xy/yz/xz
        """
        raise NotADirectoryError("magnify")

class Painter(AbstractPainter):

    def multiline(self, x):
        print("Lines: " + '->'.join(str(v) for v in x))

    def circle(self, plane, c, r):
        print("Circle: In plane %r, center at %r, radius %r" % (plane, c, r))

    def magnify(self, plane):
        print("Magnify: plane %r" % plane)

import click
@click.command()
@click.argument("action")
@click.option("--path", help="path to display")
def main(action, path):
    assert action == 'display'
    # load constructor info for the component
    import pickle
    f, kwds = pickle.load(open(path, 'rb'))
    # create component instance
    instance = f(**kwds)
    # call display method
    instance.core().display()
    return

if __name__ == '__main__': main()

# End of file 
