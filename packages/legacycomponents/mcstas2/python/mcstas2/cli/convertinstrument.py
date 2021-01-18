# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import os, sys, click
from collections import OrderedDict

from . import mcstas
@mcstas.command()
@click.argument("filename")
@click.option('--type', default='non-pyre', type=click.Choice(['pyre', 'non-pyre']))
def convertinstrument(filename=None, type='non-pyre'):
    if not os.path.exists(filename):
        raise IOError("McStas Instrument %r does not exist" % filename)
    click.echo("Converting McStas instrument %s ..." % filename)
    App().run(filename, type)
    return


class App(object):

    def run(self, input, type='pyre'):
        self._type = type
        text = open(input).read()
        from mcstas2.utils.parsers.McStasInstrumentParser import McStasInstrumentParser
        parser = McStasInstrumentParser()
        instrument = parser.parse(text)
        
        fname = os.path.basename(input)
        if sys.version_info < (3,0) and isinstance(fname, unicode):
            fname = fname.encode()
        instrname, ext = os.path.splitext(fname)

        instrument.name = instrname
        try:
            self._render(instrument)
        except:
            import traceback
            traceback.print_exc()
            print()
            self._onError()
        return

    
    def _onError(self):
        print('*'*70)
        print('This conversion script is still experimental')
        print('Please make sure:')
        print('"AT" clause and "ROTATED" clause are in different lines')
        return


    def _render(self, instrument):
        method = getattr(self, '_render_%s' % self._type.replace('-', '_'))
        return method(instrument)


    def _render_non_pyre(self, instrument):
        lines = """import mcvine, mcvine.components as mcomps
instrument = mcvine.instrument()
""".splitlines()
        lines.append('')
        import mcvine.components, mcvine
        cats = mcvine.listallcomponentcategories()
        cats = [getattr(mcvine.components, cat) for cat in cats]
        for comp in instrument.components:
            type = comp.type
            for cat in cats:
                found = hasattr(cat, type)
                if found: break
                continue
            if not found: cat = 'unknown'
            else: cat = cat.__class__.__name__
            plist = ', '.join('%s=%s' % (k,v) for k,v in sorted(comp.parameters.items()))
            if plist: plist = ', ' + plist
            lines.append('%s = mcomps.%s.%s(name=%r%s)' % (comp.name, cat, comp.type, comp.name, plist))
            # comp.position = [vector, "absolute" or "relative", reference]
            lines.append('instrument.append(%s, position=%s, orientation=%s%s)' % (
                comp.name,
                comp.position[0], comp.orientation[0],
                ', relativeTo=%s'%comp.position[2] if comp.position[1] is 'relative' else ''
                ))
            lines.append('')
            continue
        out = '%s_mcvine.py' % instrument.name
        with open(out, 'wt') as stream:
            stream.write('\n'.join(lines))
        return
    
    
    def _render_pyre(self, instrument):
        self._dumpAsJsonStr(instrument)
        self._createInstrumentScript(instrument)
        self._createInstrumentConfigurator(instrument)
        return

    
    def _dumpAsJsonStr(self, instrument):
        def comp2dict(comp):
            params = _toOrderedDictSortedByKey(comp.parameters)
            return OrderedDict(
                name = comp.name,
                type = comp.type,
                parameters = params,
                position = comp.position,
                orientation = comp.orientation,
                )
        def instr2dict(inst):
            return [comp2dict(c) for c in inst.components]
        data = instr2dict(instrument)
        import json
        out = '%s.json' % instrument.name
        json.dump(data, open(out, 'wt'))
        print('* generated instrument description in "%s"' % out)
        return

    
    def _createInstrumentConfigurator(self, instrument):
        # render
        text = InstrumentConfiguratorRenderer().render(instrument)
        text = '\n'.join(text)
        # write out
        out = 'config-%s' % instrument.name
        open(out, 'w').write(text)
        # make executable
        import os, stat
        path = os.path.abspath(out); os.chmod(path, stat.S_IRWXU)
        # done
        print('* generated instrument configurator "%s"' % out)
        return


    def _createInstrumentScript(self, instrument):
        complist = ','.join([c.name for c in instrument.components])
        d = {
            'name': instrument.name,
            'components': complist,
            }
        cmd = 'mcvine-create-instrument-simulation-application -name=%(name)s -components=%(components)s' % d
        cmd += '> /dev/null'
        if os.system(cmd):
            raise RuntimeError("%s failed"  % cmd)
        print('* generated mcvine app "%s"' % instrument.name)


    def _createPml(self, instrument):
        # obsolete
        # this is not the best way to create pml
        # plan: create the application code
        out = '%s.pml' % instrument.name
        if os.path.exists(out):
            os.remove(out)
        
        text = PmlRenderer().render(instrument)
        text = '\n'.join(text)
        open(out, 'w').write(text)
        print('* generated configuration "%s"' % out)
        return

    pass


class InstrumentConfiguratorRenderer(object):

    def render(self, instrument):
        self._reps = []
        self._indlevel = 0
        self._indstr = '  '
        w = self._write
        w('#!/usr/bin/env python')
        w('')
        w('# %s' % instrument.name)
        w('')
        # components and config method
        self.onInstrument(instrument)
        w('')
        # App
        w('from pyre.applications.Script import Script as base')
        w('class App(base):')
        self._indent()
        w('class Inventory(base.Inventory):')
        self._indent()
        w('import pyre.inventory')
        _typedict = {
            'string': 'str',
            'char *': 'str',
            'double': 'float',
            '': 'float',
            'boolean': 'bool',
            }
        def _convertTypeStr(k):
            if k in _typedict: return _typedict[k]
            return k
        for p in instrument.parameters:
            type = _convertTypeStr(p['type'])
            d = dict(
                name = p['name'],
                type = type,
                default = p['value']
                )
            w('%(name)s = pyre.inventory.%(type)s("%(name)s", default="%(default)s")' % d)
            continue
        w('pass # Inventory')
        self._outdent() # Inventory
        
        w('def main(self, *args, **kwds):')
        self._indent()
        w('d={}')
        for p in instrument.parameters:
            w('d["%(name)s"] = self.inventory.%(name)s' % p)
            continue
        w('config(**d)')
        w('return')
        self._outdent() # App.main
        
        w('def help(self):')
        self._indent() # App.help
        w('import sys, os')
        w('h = os.path.basename(sys.argv[0]) + "  "')
        w('print h,')
        s = ' '.join(
            ['--%s=%s' % (p['name'], p['value'])
             for p in instrument.parameters
             ])
        w('print "%s"' % s)
        self._outdent() # App.help
        
        self._outdent() # App
        
        w('def main():')
        self._indent()
        w('App("config-%s").run()' % instrument.name)
        self._outdent() # main
        
        w("if __name__=='__main__': main()")
        return self._reps
    

    def onInstrument(self, instrument):
        for comp in instrument.components:
            self.onComponent(comp)
            continue
        w = self._write
        w('def config(%s):' % _formatParamStr(instrument.parameters))
        self._indent()
        for l in instrument.init.splitlines():
            w(l)
            continue
        w(
            'components = [%s()]' % ', '.join(
                [c.name for c in instrument.components])
            )
        w('from mcvine.pyre_support.pml import set_instrument_parameters, PmlRenderer')
        w('class instrument: pass')
        w('instrument.name=%r' % instrument.name)
        w('instrument.components=components')
        w('set_instrument_parameters(instrument, locals())')
        w('from mcvine.pyre_support.pml import PmlRenderer')
        w('renderer = PmlRenderer()')
        w("text = '\\n'.join(renderer.render(instrument))")
        w("pml = '%s.pml'" % instrument.name)
        w("open(pml, 'wt').write(text)")
        w('return')
        self._outdent()
        return


    def onComponent(self, component):
        self._write('class %s(object):' % component.name)
        self._indent()
        for k,v in sorted(component.__dict__.items()):
            if k.startswith('_'): continue
            if isinstance(v, dict): v = _toOrderedDictSortedByKey(v)
            self._property(k,v)
            continue
        self._outdent()
        self._write('')
        return

    
    def _property(self, k, v):
        if isinstance(v, OrderedDict):
            text = '%s=%s' % (k, _od2str(v))
        else:
            text = '%s=%r' % (k,v)
        self._write(text)
        return

    
    def _write(self, text):
        t = self._indlevel * self._indstr + text
        self._reps.append(t)
        return


    def _indent(self): self._indlevel += 1
    def _outdent(self): self._indlevel -= 1


def _formatParamStr(params):
    l = []
    for p in params:
        s = '%s=%s' % (p['name'], p['value'])
        l.append(s)
        continue
    return ', '.join(l)

def _toOrderedDictSortedByKey(d):
    o = OrderedDict()
    for k, v in sorted(d.items()): o[k] = v
    return o

def _od2str(d):
    "convert ordereddict to str"
    return '{' + ', '.join('%r: %r'%(k,v) for k,v in d.items()) + '}'

from mcvine.pyre_support.pml import PmlRenderer


# version
__id__ = "$Id$"

# End of file 
