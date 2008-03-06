

#register new scatterer type
# 1. the pure python class
from mccomposite.Scatterer import Scatterer
class NeutronPrinter(Scatterer):
    def identify(self, visitor): return visitor.onNeutronPrinter(self)
    pass
# 2. the handler to construct c++ engine
def onNeutronPrinter(self, printer):
    shape = printer.shape()
    cshape = shape.identify(self)
    return self.factory.neutronprinter( cshape )
# 3. the handler to call python bindings 
def neutronprinter(self, cshape):
    from neutron_printer2 import cScatterer
    return cScatterer( cshape )
# 4. register the new class and handlers
import mccomposite
mccomposite.register( NeutronPrinter, onNeutronPrinter,
                      {'BoostPythonBinding':neutronprinter} )


