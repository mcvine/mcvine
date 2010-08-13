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
    if not reg1 and not reg2:
        return 
    if not reg1:
        return None, reg2['name']
    if not reg2:
        return reg1['name'], None

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
    
    components1 = reg1.get('components') or {}
    components2 = reg2.get('components') or {}
    if not components1 and not components2:
        return diff
        
    cdiff = diff['components'] = {}
    for name, comp1 in components1.iteritems():
        comp2 = components2.get(name)
        cdiff[name] = compare(comp1, comp2)
        continue

    for name, comp2 in components2.iteritems():
        if name in components1.keys(): continue
        cdiff[name] = compare(None, comp2)
    
    return diff


def report(diff, indent=0):
    ret = []
    pre = ' ' * indent
    ret.append(pre + '[%s]' % diff['name'])
    for k, v in diff.iteritems():
        if k in ['name', 'components']: continue
        v1, v2 = v
        ret.append(pre + ' - %s' % k)
        ret.append(pre + '  < %s' % v1)
        ret.append(pre + '  > %s' % v2)
        continue
    
    comps = diff.get('components')
    if comps:
        ret.append(pre + ' - components:')
        for name, c in comps.iteritems():
            if isinstance(c, tuple):
                v1, v2 = c
                ret.append(pre + '  [%s]' % name)
                ret.append(pre + '   < %s' % v1)
                ret.append(pre + '   > %s' % v2)
                continue
            
            ret += report(c, indent+2)
            
    return ret


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


def test2():
    reg1 = {'name': 'a', 
            'k1': 3,
            'k2': 'a',
            'components': {
                'integrator': {
                  'name': 'montecarlo',
                  'p1': 1e10
                  },
                'optimizer': {
                  'name': 'abc',
                  },
                }
            }
    reg2 = {'name': 'a', 
            'k1': 5,
            'k2': 'a',
            'components': {
                'integrator': {
                  'name': 'montecarlo',
                  'p1': 2e10
                  }
                }
            }
    diff = compare(reg1, reg2)
    print '\n'.join(report(diff))
    assert diff == {
        'name': 'a', 'k1': (3,5),
        'components': {
            'integrator': {
                'p1': (1e10, 2e10), 
                'name': 'montecarlo'
                },
            'optimizer': ('abc', None),
            }
        }
    return


def main():
    test()
    test2()
    return 


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
