import mcvine, mcvine.components
from mcni.AbstractComponent import AbstractComponent
class WithBug(AbstractComponent):
    def __init__(self, name, trigger):
        if trigger == 'ctor':
            raise RuntimeError(name)
        self.trigger = trigger
        self.name = name
    def process(self, neutrons):
        if self.trigger == 'process':
            raise RuntimeError('processing')
        return neutrons

def instrument(trigger='ctor'):
    instrument = mcvine.instrument()
    # add source
    source = WithBug('source', trigger=trigger)
    instrument.append(source, position=(0,0,0))
    return instrument
