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



from mccomponents.homogeneous_scatterer.bindings.BoostPythonBinding \
     import BoostPythonBinding, extend

import mccomponents.mccomponentsbp as b
import mccomposite.mccompositebp as b1


class New:

    def gridsqe(self, qbegin, qend, qstep,
                ebegin, eend, estep,
                s ):
        '''gridsqe: S(Q,E) on grid

        qbegin, qend, qstep: Q axis boundaries. qend must be larger than qbegin+qstep*Nqbins
        ebegin, eend, estep: E axis boundaries. eend must be larger than ebegin+estep*NEbins
        s: numpy array of S
        '''
        shape = s.shape
        assert len(shape) == 2
        assert shape[0] == int( (qend-qbegin)/qstep ), (
            'qend: %s, qbegin: %s, qstep: %s, shape0: %s' % (
            qend, qbegin, qstep, shape[0]) )
        assert shape[1] == int( (eend-ebegin)/estep )
        size = shape[0] * shape[1]
        svector = b.vector_double( size )
        saveshape = s.shape
        s.shape = -1,
        svector[:] = s
        s.shape = saveshape
        fxy = b.new_fxy(
            qbegin, qend, qstep,
            ebegin, eend, estep,
            svector)
        return b.GridSQE( fxy )

    def sqeFromExpression(self, expr):
        '''sqeFromExpression: S(Q,E) from analystic expreession
        '''
        expr = str(expr)
        return b.SQE_fromexpression(expr)

    def sqe_energyfocusing_kernel(
            self, absorption_cross_section, scattering_cross_section,
            unitcell_vol,
            sqe, Qrange, Erange, Ef, dEf):
        '''sqekernel: a kernel takes S(Q,E) a functor and has a final energy focusing

        absorption_cross_section: absorption cross section
        scattering_cross_section: scattering cross section
        sqe: S(Q,E) functor
        Qrange, Erange: range of Q and E
        Ef, dEf: final energy focusing
        '''
        Emin, Emax = Erange
        Qmin, Qmax = Qrange
        return b.SQE_EnergyFocusing_Kernel(
            absorption_cross_section, scattering_cross_section,
            unitcell_vol,
            sqe, Qmin, Qmax, Emin, Emax, Ef, dEf )

    def sqekernel(self, absorption_cross_section, scattering_cross_section,
                  unitcell_vol,
                  sqe, Qrange, Erange):
        '''sqekernel: a kernel takes S(Q,E) a functor

        absorption_cross_section: absorption cross section
        scattering_cross_section: scattering cross section
        sqe: S(Q,E) functor
        Qrange, Erange: range of Q and E
        '''
        Emin, Emax = Erange
        Qmin, Qmax = Qrange
        return b.SQEkernel(
            absorption_cross_section, scattering_cross_section,
            unitcell_vol,
            sqe, Qmin, Qmax, Emin, Emax )
    

    def gridsq(self, qbegin, qend, qstep, s ):
        '''gridsq: S(Q) on grid

        qbegin, qend, qstep: Q axis
        s: numpy array of S
        '''
        shape = s.shape
        assert len(shape) == 1
        assert shape[0] == int( (qend-qbegin)/qstep +0.5 ), (
            'qend: %s, qbegin: %s, qstep: %s, shape0: %s' % (
            qend, qbegin, qstep, shape[0]) )
        size = shape[0]
        
        svector = b.vector_double( size )
        saveshape = s.shape
        s.shape = -1,
        svector[:] = s
        s.shape = saveshape
        
        fx = b.new_fx(qbegin, qend, qstep, svector)
        
        return b.GridSQ( fx )

    
    def sqFromExpression(self, expr):
        '''sqFromExpression: S(Q) from analystic expreession
        '''
        expr = str(expr)
        return b.SQ_fromexpression(expr)

    
    def sqkernel(
            self,
            absorption_coefficient, scattering_coefficient,
            sq, Qrange):
        '''sqkernel: a kernel takes S(Q) a functor

        absorption_coefficient: 1/absorption_length
        scattering_coefficient: 1/scattering_length
        sq: S(Q) functor
        Qrange: range of Q
        '''
        Qmin, Qmax = Qrange
        return b.SQkernel(
            absorption_coefficient, scattering_coefficient,
            sq, Qmin, Qmax)
    

    def isotropickernel(self, absorption_cross_section, scattering_cross_section):
        '''isotropickernel: a kernel scatters isotropically and elastically

        absorption_cross_section: absorption cross section
        scattering_cross_section: scattering cross section
        '''
        return b.IsotropicKernel(absorption_cross_section, scattering_cross_section)


    def dgssxreskernel(
            self,
            target_position, target_radius,
            tof_at_target, dtof,
            absorption_cross_section, scattering_cross_section):
        from mccomposite.bindings.BoostPythonBinding import binding as _b
        target_position = _b.Vector3_double(*target_position)
        return b.DGSSXResKernel(
            target_position, target_radius,
            tof_at_target, dtof,
            absorption_cross_section, scattering_cross_section)


    def constantEnergyTransferKernel(self, E, absorption_coefficient, scattering_coefficient):
        '''constantenergytransferkernel: a kernel scatters isotropically with fixed energy transfer

        E: energy transfer
        absorption_coefficient: 1/absorption_length
        scattering_coefficient: 1/scattering_length
        '''
        return b.ConstantEnergyTransferKernel(E, absorption_coefficient, scattering_coefficient)


    def E_Q_Kernel(
        self,
        E_Q, S_Q='1', 
        Qmin = 0., Qmax = 10.,
        absorption_coefficient=1., scattering_coefficient=1.
        ):
        '''
        S(Q,E) = S(E) * delta(E-E(Q))

        E_Q: E(Q). str. ex: Q*Q/3.5
        S_Q: S(Q). str. ex: 1.
        Qmin, Qmax: range of Q. AA**-1
        absorption_coefficient: absorption coefficient (m**-1)
        scattering_coefficient: scattering coefficient (m**-1)
        '''
        return b.create_E_Q_Kernel(
            E_Q, S_Q, 
            Qmin, Qmax,
            absorption_coefficient, scattering_coefficient)


    def Broadened_E_Q_Kernel(
        self,
        E_Q, S_Q='1', sigma_Q="0.5*Q",
        Qmin = 0., Qmax = 10.,
        absorption_coefficient=1., scattering_coefficient=1.
        ):
        '''
        S(Q,E) = S(E) * delta(E-E(Q))

        E_Q: E(Q). str. ex: Q*Q/3.5
        S_Q: S(Q). str. ex: 1.
        sigma_Q: sigma(Q). str. ex: Q/2
        Qmin, Qmax: range of Q. AA**-1
        absorption_coefficient: absorption coefficient (m**-1)
        scattering_coefficient: scattering coefficient (m**-1)
        '''
        return b.create_Broadened_E_Q_Kernel(
            E_Q, S_Q, sigma_Q,
            Qmin, Qmax,
            absorption_coefficient, scattering_coefficient)


    def E_vQ_Kernel(
        self,
        E_Q, S_Q='1', 
        Emax = 10.,
        absorption_coefficient=1., scattering_coefficient=1.
        ):
        '''
        S(Q,E) = S(E) * delta(E-E(Q))

        E_Q: E(Q). str. ex: sin(Qx+Qy+Qz)
        S_Q: S(Q). str. ex: 1.
        Emax: meV
        absorption_coefficient: absorption coefficient (m**-1)
        scattering_coefficient: scattering coefficient (m**-1)
        '''
        return b.create_E_vQ_Kernel(
            E_Q, S_Q,
            Emax,
            absorption_coefficient, scattering_coefficient)


    def constantQEKernel(self, Q, E, absorption_coefficient, scattering_coefficient):
        '''constantqekernel: a kernel scatters isotropically with fixed momentum and energy transfer

        Q: momentum transfer
        E: energy transfer
        absorption_coefficient: absorption coefficient (m**-1)
        scattering_coefficient: scattering coefficient (m**-1)
        '''
        return b.ConstantQEKernel(Q, E, absorption_coefficient, scattering_coefficient)

    
    def constantvQEKernel(self, Q, E, dE, absorption_coefficient, scattering_coefficient):
        '''constantvqekernel: a kernel scatters with fixed momentum and energy transfer

        Q: momentum transfer, vector
        E: energy transfer
        dE: energy broadening
        absorption_coefficient: absorption coefficient (m**-1)
        scattering_coefficient: scattering coefficient (m**-1)
        '''
        return b.ConstantvQEKernel(
            Q[0], Q[1], Q[2], E, dE, 
            absorption_coefficient, scattering_coefficient)

    
    pass # end of BoostPythonBinding


extend( New )



# version
__id__ = "$Id$"

# End of file 
