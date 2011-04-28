
## patch the interface of Neutron::Events boost python binding

from mcni.mcnibp import vector_Event


original__str__ = vector_Event.__str__
def __str__(self):
    if len(self)>10: return original__str__(self)
    return ', '.join( [ '%s' % n for n in self ] )

vector_Event.__str__ = __str__
    


from mcni.mcnibp import NeutronEventBuffer
def NEB_appendNeutrons(self, neutrons, startindex=None, endindex=None):
    """append neutrons to the end of this neutron buffer

    neutrons: the neutron buffer from which the new neutrons are to be obtained
            and appended to this buffer
    startindex, endindex: define the region from which neutrons are obtained
    """
    if startindex is None:
        startindex = 0
    if endindex is None:
        endindex =  len(neutrons)
    self.append(neutrons, startindex, endindex)
    return
NeutronEventBuffer.appendNeutrons = NEB_appendNeutrons
NEB_snapshot_o = NeutronEventBuffer.snapshot
def NEB_snapshot(self, n=None):
    """take a snapshot of this neutron buffer, remove the invalid
    ones (prob<0), and return a new neutron buffer.
    
    n: the number of neutrons in this buffer from which
        the snapshot will be take. None means all neutrons
    """
    if n is None:
        n = len(self)
    return NEB_snapshot_o(self, n)
NeutronEventBuffer.snapshot = NEB_snapshot
