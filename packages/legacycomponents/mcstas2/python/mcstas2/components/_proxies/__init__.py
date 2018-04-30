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
    d = dict(locals()); exec code in d; kls = d[name]
    factory = module.factory
    def new_factory(*args, **kwds):
        return kls(factory, *args, **kwds)
    new_factory.__doc__ = factory.__doc__
    new_factory.info = factory.info
    new_factory.__name__ = name
    return new_factory

def getProxy(category, type):
    thispackage = 'mcstas2.components._proxies'
    package = '.'.join([thispackage, category, type])
    try:
        package = _import(package)
    except ImportError:
        import journal
        debug = journal.debug(thispackage)
        import traceback
        debug.log(traceback.format_exc())
        from . import default as package
    return getattr(package, 'Component')


def _import(package):
    return __import__(package, {}, {}, [''])
