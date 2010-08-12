#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''compare two registries. both of them must be dictionaries
created by RegstryToDict.Renderer
'''

def compare(reg1, reg2):
    diff = {}
    diff['name'] = reg1['name']
    for k, v1 in reg1.iteritems():
        if k == 'components':
            continue
        v2 = reg2.get(k)
        if v1 != v2: 
            diff[k] = v1, v2
        continue

    for k, v2 in reg2.iteritems():
        if k in reg1.keys(): continue
        v1 = reg1.get(k)
        if v1 != v2:
            diff[k] = v1, v2
    
    components1 = reg1.get('components')
    components2 = reg2.get('components')
    if not components1 or not components2:
        if components1 or components2:
            diff['components'] = components1, components2
            return
        
    cdiff = diff['components'] = {}
    for name, comp1 in components1.iteritems():
        comp2 = components2.get(name)
        cdiff[name] = compare(comp1, comp2)
        continue
    
    return diff


def report(diff):
    return


def test():
    reg1 = {'name': 'a', 
            'k1': 3,
            'k2': 'a',
            }
    reg2 = {'name': 'a', 
            'k1': 5,
            'k2': 'a',
            }
    diff = compare(reg1, reg2)
    assert diff == {'name': 'a', 'k1': (3,5)}
    return


def main():
    test()
    return 


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
