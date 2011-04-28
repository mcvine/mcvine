
## patch the interface of Neutron::Events boost python binding

from mcni.mcnibp import vector_Event


original__str__ = vector_Event.__str__
def __str__(self):
    if len(self)>10: return original__str__(self)
    return ', '.join( [ '%s' % n for n in self ] )

vector_Event.__str__ = __str__
    


def NEB_appendNeutrons(self, neutrons, startindex, endindex):
    """append neutrons to the end of this neutron buffer

    neutrons: the neutron buffer from which the new neutrons are to be obtained
            and appended to this buffer
    startindex, endindex: define the region from which neutrons are obtained
    """
    self.append(neutrons, startindex, endindex)
    return
from mcni.mcnibp import NeutronEventBuffer
NeutronEventBuffer.appendNeutrons = NEB_appendNeutrons
