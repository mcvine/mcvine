def createFactory(category, type, module):
    """create factory method

    This is called by Registry.register.
    module is the auto-generated module that wraps a mcstas component.
    it should contains a "factory" method.
    """
    # it is a proxy class
    Proxy = getProxy(category, type)
    name = "%s_%s" % (category.capitalize(), type.capitalize())
    code = "class %s(Proxy): pass" % (name,)
    d = dict(locals()); exec(code, d); kls = d[name]
    factory = module.factory
    def new_factory(*args, **kwds):
        return kls(factory, *args, **kwds)
    new_factory.__doc__ = factory.__doc__
    new_factory.info = factory.info
    new_factory.__name__ = name
    new_factory.__module__ = factory.__module__
    return new_factory

def getProxy(category, type):
    thispackage = 'mcstas2.components._proxies'
    package = '.'.join([thispackage, category, type])
    # try the particular type first
    try:
        package = _import(package)
    except ImportError:
        # try category default
        package = '.'.join([thispackage, category, 'default'])
        try:
            package = _import(package)
        except ImportError:
            # last resort
            from . import default as package
    return getattr(package, 'Component')


def _import(package):
    return __import__(package, {}, {}, [''])
