# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#
# This module was copied from yxqd/nimg

def loadYmlConfig(path):
    "load yaml config file from the given path and return a python object"
    # impl note: yml load returns a dict, converts to a py obj assisted by Struct below
    import yaml
    f = open(path)
    d = yaml.safe_load(f)
    f.close()
    return Struct(d)

# This class was copied from a StackOverflow thread
class Struct:
    '''The recursive class for building and representing objects with.'''
    def __init__(self, obj):
        for k, v in obj.items():
            setattr(self, k, _struct(v))
    def __getitem__(self, val):
        return self.__dict__[val]
    def __setitem__(self, key, val):
        self.__dict__[key] = val
        return val
    def __repr__(self):
        return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
                                      (k, v) in self.__dict__.items()))

def _struct(v):
    if isinstance(v, dict):
        return Struct(v)
    elif isinstance(v, list):
        return map(_struct, v)
    else:
        return v
                                     
# End of file 
