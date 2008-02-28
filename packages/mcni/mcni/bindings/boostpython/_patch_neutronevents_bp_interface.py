
## patch the interface of Neutron::Events boost python binding

from mcni.mcnibp import vector_Event


original__str__ = vector_Event.__str__
def __str__(self):
    if len(self)>10: return original__str__(self)
    return ','.join( [ str(n) for n in self ] )

vector_Event.__str__ = __str__
    
