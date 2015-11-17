#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractSQE import AbstractSQE as base
class GridSQE(base):

    def __init__(self, sqehist):
        '''sqehist: a histogram instance'''
        self.sqehist = sqehist
        return
    
    def identify(self, visitor): return visitor.onGridSQE( self )

    pass  # end of AbstractSQE



#register new type
# 2. the handler of engine renderer
def onGridSQE(self, gridsqe):

    sqehist = gridsqe.sqehist

    qbb = sqehist.axisFromName('Q').binBoundaries().asNumarray()
    qbegin, qend, qstep = qbb[0], qbb[-1], qbb[1]-qbb[0]
    
    ebb = sqehist.axisFromName('energy').binBoundaries().asNumarray()
    ebegin, eend, estep = ebb[0], ebb[-1], ebb[1]-ebb[0]

    s = sqehist.data().storage().asNumarray()
    
    return self.factory.gridsqe(
        qbegin, qend, qstep,
        ebegin, eend, estep,
        s )


# 3. the handler to call python bindings
def gridsqe(self, qbegin, qend, qstep,
            ebegin, eend, estep,
            s ):
    
    shape = s.shape
    assert len(shape) == 2
    assert shape[0] == int( (qend-qbegin)/qstep )
    assert shape[1] == int( (eend-ebegin)/estep )
    size = shape[0] * shape[1]
    
    import mccomponents.mccomponentsbp as b
    svector = b.vector_double( size )
    s.shape = -1,
    svector[:] = s

    fxy = b.new_fxy(
        qbegin, qend, qstep,
        ebegin, eend, estep,
        svector)
    
    return b.GridSQE( fxy )


import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register (
    GridSQE, onGridSQE,
    {'BoostPythonBinding':gridsqe} )




# version
__id__ = "$Id$"

# End of file 
