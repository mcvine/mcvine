# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2008-2013  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



class PmlRenderer(object):

    """
    render pml out of an instrument data object (see below)
    
class Instrument:

    components = None


class Component:

    type = None
    name = None
    parameters = None
    position = None
    orientation = None

    """

    def render(self, instrument):
        self._reps = []
        self._indlevel = 0
        self._indstr = '  '
        self._write('<?xml version="1.0"?>')
        self._write('<inventory>')
        self._indent()
        self.onInstrument(instrument)
        self._outdent()
        self._write('</inventory>')
        return self._reps
    

    def onInstrument(self, instrument):
        self._write('<component name="%s">' % instrument.name)
        self._indent()

        self._property('sequence', ','.join([c.name for c in instrument.components]))
        for c in instrument.components:
            self._property(c.name, c.type)
            continue

        self.onGeometer(instrument)
        self._write('')

        self._property('multiple-scattering', 'off')
        
        self._property('ncount', "1e6")
        self._property('buffer_size', 100000)
        
        self._property('output-dir', 'out')
        self._property('overwrite-datafiles', 'off')
        self._write('')

        for c in instrument.components:
            self.onComponent(c)
            self._write('')
            continue
        
        self._outdent()
        self._write('</component>')
        return


    def onGeometer(self, instrument):
        self._write('<component name="geometer">')
        self._indent()
        for c in instrument.components:
            k = c.name
            v = self._geometerEntry(c.position, c.orientation)
            self._property(k,v)
            continue
        self._outdent()
        self._write('</component>')
        return


    def onComponent(self, component):
        self._write('<component name="%s">' % component.name)
        self._indent()
        for k,v in component.parameters.iteritems():
            v = self._formatValue(v)
            self._property(k,v)
            continue
        self._outdent()
        self._write('</component>')
        return

    
    def _formatValue(self, value):
        return value
    

    def _geometerEntry(self, position, orientation):
        position = self._coord(position)
        orientation = self._coord(orientation)
        return ','.join((position, orientation))


    def _coord(self, coord):
        v, relation, to = coord
        if relation.lower() == 'absolute' or \
                relation.lower() == 'relation' and to.lower() == 'absolute':
            return str(v)
        else:
            assert relation.lower() == 'relative'
            return 'relative(%s, to="%s")' % (v, to)


    def _property(self, k, v):
        t = '<property name="%s">%s</property>' % (k,v)
        self._write(t)
        return


    def _write(self, text):
        t = self._indlevel * self._indstr + text
        self._reps.append(t)
        return


    def _indent(self): self._indlevel += 1
    def _outdent(self): self._indlevel -= 1


def set_instrument_parameters(instrument, d):
    """set instrument parameters using values stored in dictionary d
    
    This method is used by instrument configuration script generated
    by mcvine-convert-mcstas-instrument
    """
    def getdict(comp):
        d = {}
        for k in dir(comp):
            if k.startswith('_'): continue
            d[k] = getattr(comp, k)
            continue
        return d
    def set(comp, d):
        for k,v in d.iteritems():
            setattr(comp, k, v)
            continue
        return
    comps = instrument.components
    for comp in comps:
        dest = getdict(comp)
        propagate_values(dest, src=d)
        set(comp, dest)
        continue
    return


def propagate_values(dest, src):
    """propagate values from the given source dictionary src
    into the destination dest
    """
    if isinstance(dest, tuple) or isinstance(dest, list):
        t = type(dest)
        dest = [propagate_values(item, src) for item in dest]
        return t(dest)
    if isinstance(dest, dict):
        for k, v in dest.iteritems():
            if k.startswith('_'): continue
            v = propagate_values(v, src)
            dest[k] = v
            continue
        return dest
    try:
        dest = eval(dest, src)
    except: pass
    return dest


# version
__id__ = "$Id$"

# End of file 
