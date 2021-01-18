from .base import Component as base


class Component(base):

    def _dumpData(self):
        print("%s has not implemented _dumpData" % type(self))
        
    def create_pps(self):
        print("%s has not implemented create_pps" % type(self))

    pass

# End of file 
