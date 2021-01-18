
def make_subclass( klasses ):
    "make a subclass of the given classes"
    class kls(*klasses): pass
    return kls

