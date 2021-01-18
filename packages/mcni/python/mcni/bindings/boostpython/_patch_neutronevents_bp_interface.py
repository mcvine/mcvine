
## patch the interface of Neutron::Events boost python binding

from mcni.mcnibp import vector_Event, Position_double, Velocity_double, NeutronState, NeutronSpin


original__str__ = vector_Event.__str__
def __str__(self):
    if len(self)>10: return original__str__(self)
    return ', '.join( [ '%s' % n for n in self ] )

vector_Event.__str__ = __str__


def vector3_str(self):
    return str(list(self))
Position_double.__str__ = Velocity_double.__str__ = vector3_str
Position_double.__repr__ = Velocity_double.__repr__ = vector3_str


def spin_str(self):
    return '(%s, %s)' % (self.s1, self.s2)
NeutronSpin.__str__ = NeutronSpin.__repr__ = spin_str


def state_str(self):
    return "State(position=%r, velocity=%r, spin=%r)" % (
        self.position, self.velocity, self.spin)
NeutronState.__str__ = state_str


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
    if not isinstance(endindex, int):
        _ = endindex
        endindex = int(_)
        assert _==endindex
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

def NEB_tonpyarr(self):
    from mcni.neutron_storage import neutrons_as_npyarr, ndblsperneutron
    arr = neutrons_as_npyarr(self)
    arr.shape = -1, ndblsperneutron
    return arr
NeutronEventBuffer.to_npyarr = NEB_tonpyarr


def NEB_fromnpyarr(self, arr):
    # 
    from mcni.neutron_storage import ndblsperneutron
    arr.shape = -1, ndblsperneutron

    # # of events
    N = len(arr)
    
    # cevents
    cevents = cevents_from_npyarr(arr)

    # resize myself so we can accept events from array
    from mcni import neutron
    ev = neutron()
    self.resize(N, ev)
    
    # copy
    self.fromCevents(cevents, N)
    
    return
NeutronEventBuffer.from_npyarr = NEB_fromnpyarr


def cevents_from_npyarr(npyarr):
    '''convert a numpy array to a boost-python instance of Neutron::cEvent pointer'''
    try:
        from danse.ins.numpyext import getdataptr
    except ImportError:
        from numpyext import getdataptr
        import warnings
        warnings.warn("Using old numpyext. Should use danse.ins.numpyext")
    
    ptr = getdataptr( npyarr )
    try:
        from danse.ins import bpext
    except ImportError:
        import bpext
        import warnings
        warnings.warn("Using old bpext. Should use danse.ins.bpext")
    import mcni._mcni
    cevents = bpext.wrap_ptr( ptr, 'cNeutronEvent' )
    cevents.origin = npyarr
    return cevents


