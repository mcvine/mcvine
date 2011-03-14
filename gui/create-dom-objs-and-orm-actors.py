#!/usr/bin/env python


def main():
    from mcvine import listallcomponentcategories, listcomponentsincategory
    for category in listallcomponentcategories():
        print ' - components in %r category' % (category,)
        comps = listcomponentsincategory(category)
        for comp, suppliername in comps:
            createDOMObj(comp)
            createOrmActor(comp)
    return


domobj_template = """# -*- Python -*-

from AbstractNeutronComponent import AbstractNeutronComponent as base
class %(name)s(base):
    abstract = False

InvBase=base.Inventory
class Inventory(InvBase):
    dbtablename = '%(tablename)s'

%(name)s.Inventory = Inventory
del Inventory

from _ import o2t, NeutronComponentTableBase
%(name)sTable = o2t(%(name)s, {'subclassFrom': NeutronComponentTableBase})
"""

import os
def createDOMObj(comp):
    p = os.path.join('mcvineui', 'dom', 'neutron_components', '%s.py' % comp)
    d = {'name': comp, 'tablename': comp.lower()}
    c = domobj_template % d
    open(p, 'w').write(c)
    return



ormactor_template = """# -*- Python -*-

from mcvineui.dom.neutron_components.%(name)s import %(name)s
from mcvineui.actors.NeutronComponentOrmActorFactory import factory
Actor = factory(%(name)s, needauthorization=False)
def actor():
    return Actor('orm/%(tablename)s')

"""

def createOrmActor(comp):
    d = {'name': comp, 'tablename': comp.lower()}
    p = os.path.join('content', 'components', 'actors', 'orm', '%s.odb' % d['tablename'])
    c = ormactor_template % d
    open(p, 'w').write(c)
    return



if __name__ == '__main__': main()
