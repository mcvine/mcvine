# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# auto discovery
def findComponents(package='mcvineui.dom.neutron_components'):
    from mcvineui.dom.AbstractNeutronComponent import AbstractNeutronComponent
    pkg = __import__(package, {}, {}, [''])
    import os
    dir = os.path.dirname(pkg.__file__)
    entries = os.listdir(dir)
    comps = []
    for entry in entries:
        name, ext = os.path.splitext(entry)        
        if ext not in ['.py', '.pyc']: continue
        m = __import__('%s.%s' % (package, name), {}, {}, [''])
        cls = getattr(m, name, None)
        if not cls: continue
        try:
            issubkls = issubclass(cls, AbstractNeutronComponent)
        except:
            issubkls = False
        if not issubkls: continue
        if cls.abstract: continue
        if cls in comps: continue
        comps.append(cls)
        continue
    return comps



def _typename(kls):
    pre = '.'.join(kls.__module__.split('.')[2:])
    post = kls.__name__
    return '%s.%s' % (pre, post)
typenames = [_typename(kls) for kls in findComponents()]


getTypes = findComponents

# version
__id__ = "$Id$"

# End of file 
