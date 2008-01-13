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


from mccomponents.homogeneous_scatterer.Kernel import Kernel
class SQEkernel(Kernel):

    def __init__(self,
                 absorption_cross_section = None,
                 scattering_cross_section = None,
                 SQE = None, Qrange = None, Erange = None,
                 ):
        '''new S(Q,E) kernel
  Inputs:
    absorption_cross_section, scattering_cross_section: cross sections
    SQE: S(Q,E) functor
    Qrange: Q range (min, max)
    Erange: E range (min, max)
    '''
        self.absorption_cross_section = absorption_cross_section
        self.scattering_cross_section = scattering_cross_section
        self.SQE = SQE
        self.Qrange = Qrange; self.Erange = Erange
        return
        
    def identify(self, visitor): return visitor.onSQEkernel(self)
    
    pass


#register new kernel type
# 2. the handler to construct c++ engine
def onSQEkernel(self, sqekernel):
    
    t = sqekernel

    import units
    Erange = t.Erange
    Erange = self._unitsRemover.remove_unit( Erange, units.energy.meV )

    Qrange = t.Qrange
    Qrange = self._unitsRemover.remove_unit( Qrange, 1./units.length.angstrom )

    csqe = t.SQE.identify(self)

    abs = t.absorption_cross_section
    sctt = t.scattering_cross_section
    if abs is None or sctt is None:
        #need to get cross section from sample assembly representation
        # svn://danse.us/inelastic/sample/.../sampleassembly
        #origin is a node in the sample assembly representation
        origin = t.scatterer_origin
        from sampleassembly import cross_sections
        abs, inc, coh = cross_sections( origin )
        sctt = inc + coh
        pass

    abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
    
    return self.factory.sqekernel(
        abs, sctt,
        csqe, Erange, Qrange )


# 3. the handler to call python bindings
def sqekernel(self, absorption_cross_section, scattering_cross_section,
              sqe, Erange, Qrange):
    import mccomponents.mccomponentsbp as b
    Emin, Emax = Erange
    Qmin, Qmax = Qrange
    return b.SQEkernel(
        absorption_cross_section, scattering_cross_section,
        sqe, Emin, Emax, Qmin, Qmax )


import mccomponents.homogeneous_scatterer as hs
# 4. register the new class and handlers
hs.register (
    SQEkernel, onSQEkernel,
    {'BoostPythonBinding':sqekernel} )


# version
__id__ = "$Id$"

# End of file 
