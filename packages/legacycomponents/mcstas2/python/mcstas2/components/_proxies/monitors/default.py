from .base import Component as base


class Component(base):

    def _dumpData(self):
        print "%s has not implemented _get_histogram" % type(self)
        
    def create_pps(self):
        print "%s has not implemented _get_histogram" % type(self)

    pass

# End of file 
