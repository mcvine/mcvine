__doc__ = "collection of components"

from . import listallcomponentcategories, listcomponentsincategory, componentfactory
for cat in listallcomponentcategories():
    class K(object):
        'Component category %r' % cat
        pass
    K.__name__ = cat
    _ = K()
    exec "%s=_" % cat
    for name, supplier in listcomponentsincategory(cat):
        setattr(_, name, componentfactory(cat, name, supplier))
    continue
    

