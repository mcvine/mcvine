#!/usr/bin/env python
#
#



class ComputationEngineRendererExtension:

    def onGridSQE(self, gridsqe):
        sqehist = gridsqe.sqehist
        # Q boundaries
        qbb = sqehist.axisFromName('Q').binBoundaries().asNumarray()
        qbegin, qend, qstep = qbb[0], qbb[-1], qbb[1]-qbb[0]
        try:
            ebb = sqehist.axisFromName('E').binBoundaries().asNumarray()
        except KeyError:
            ebb = sqehist.axisFromName('energy').binBoundaries().asNumarray()
        # E boundaries
        ebegin, eend, estep = ebb[0], ebb[-1], ebb[1]-ebb[0]
        # S
        s = sqehist.data().storage().asNumarray()
        # +0.5*step makes sure it is larger than qbegin+N*qstep
        return self.factory.gridsqe(
            qbegin, qend+.5*qstep, qstep,
            ebegin, eend+.5*estep, estep,
            s )

    def onSQE_fromexpression(self, sqe_fromexpression):
        expr = sqe_fromexpression.expression
        return self.factory.sqeFromExpression(expr)

    def onSQEkernel(self, sqekernel):
        
        t = sqekernel
        
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
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin, include_density=False)
            sctt = inc + coh
            pass

        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), units.length.meter**2)
        
        unitcell_vol = t.unitcell_vol
        if unitcell_vol is None:
            origin = t.scatterer_origin
            structure = origin.phase.unitcell
            unitcell_vol = structure.lattice.volume
            # convert to meter^3
            unitcell_vol *= 1.e-30
        
        return self.factory.sqekernel(
            abs, sctt, unitcell_vol,
            csqe, Qrange, Erange )


    def onSQE_EnergyFocusing_Kernel(self, sqekernel):
        t = sqekernel
        Erange = t.Erange
        Erange = self._unitsRemover.remove_unit( Erange, units.energy.meV )
        Qrange = t.Qrange
        Qrange = self._unitsRemover.remove_unit( Qrange, 1./units.length.angstrom )
        Ef = t.Ef; dEf = t.dEf
        Ef = self._unitsRemover.remove_unit(Ef, units.energy.meV)
        dEf = self._unitsRemover.remove_unit(dEf, units.energy.meV)
        csqe = t.SQE.identify(self)
        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section
        print('onSQE_EnergyFocusing_Kernel', abs, sctt)
        if abs is None and sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin, include_density=False)
            sctt = inc + coh
        elif abs is None or sctt is None:
            raise RuntimeError("Please specify both absorption and scattering cross sections")

        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), units.length.meter**2)
        unitcell_vol = t.unitcell_vol
        if unitcell_vol is None:
            origin = t.scatterer_origin
            structure = origin.phase.unitcell
            unitcell_vol = structure.lattice.volume
            # convert to meter^3
            unitcell_vol *= 1.e-30
        print('onSQE_EnergyFocusing_Kernel', unitcell_vol)
        return self.factory.sqe_energyfocusing_kernel(
            abs, sctt, unitcell_vol,
            csqe, Qrange, Erange, Ef, dEf)


    def onGridSvQ(self, gridsvq):
        svqhist = gridsvq.svqhist
        qxbb = svqhist.axisFromName('Qx').binBoundaries().asNumarray()
        qybb = svqhist.axisFromName('Qy').binBoundaries().asNumarray()
        qzbb = svqhist.axisFromName('Qz').binBoundaries().asNumarray()
        qxbegin, qxend, qxstep = qxbb[0], qxbb[-1], qxbb[1]-qxbb[0]
        qybegin, qyend, qystep = qybb[0], qybb[-1], qybb[1]-qybb[0]
        qzbegin, qzend, qzstep = qzbb[0], qzbb[-1], qzbb[1]-qzbb[0]
        s = svqhist.data().storage().asNumarray()
        return self.factory.gridsvq(
            qxbegin, qxend+qxstep/10, qxstep,
            qybegin, qyend+qystep/10, qystep,
            qzbegin, qzend+qzstep/10, qzstep,
            s )


    def onGridSQ(self, gridsq):
        sqhist = gridsq.sqhist
        
        qbb = sqhist.axisFromName('Q').binBoundaries().asNumarray()
        qbegin, qend, qstep = qbb[0], qbb[-1], qbb[1]-qbb[0]
        
        s = sqhist.data().storage().asNumarray()
        
        return self.factory.gridsq(
            qbegin, qend+0.01*qstep, qstep,
            s )


    def onSQ_fromexpression(self, sq_fromexpression):
        expr = sq_fromexpression.expression
        return self.factory.sqFromExpression(expr)


    def onSQkernel(self, sqkernel):
        t = sqkernel
        Qrange = t.Qrange
        Qrange = self._unitsRemover.remove_unit( Qrange, 1./units.length.angstrom )
        csq = t.SQ.identify(self)
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            abs, sctt, inc, coh = self._getXS(sqkernel)
            pass
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        return self.factory.sqkernel(abs, sctt, csq, Qrange)


    def onSvQkernel(self, svqkernel):
        t = svqkernel
        csvq = t.SvQ.identify(self)
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient
        if abs is None or sctt is None:
            abs, sctt, inc, coh = self._getXS(svqkernel)
            pass
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        return self.factory.svqkernel(abs, sctt, csvq)

    def onIsotropicKernel(self, kernel):
        t = kernel

        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin )
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        return self.factory.isotropickernel(abs, sctt)


    def onDGSSXResKernel(self, kernel):
        t = kernel

        abs = t.absorption_cross_section
        sctt = t.scattering_cross_section

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections( origin )
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( 
            (abs, sctt), 1./units.length.meter )
        target_position = self._unitsRemover.remove_unit(
            t.target_position, units.length.meter)
        target_radius = self._unitsRemover.remove_unit(
            t.target_radius, units.length.meter)
        tof_at_target = self._unitsRemover.remove_unit(
            t.tof_at_target, units.time.second)
        dtof = self._unitsRemover.remove_unit(
            t.dtof, units.time.second)
        return self.factory.dgssxreskernel(
            target_position, target_radius,
            tof_at_target, dtof,
            abs, sctt)


    def onConstantEnergyTransferKernel(self, kernel):
        t = kernel
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            abs, sctt, inc, coh = self._getXS(kernel)
            pass
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        E = self._unitsRemover.remove_unit(kernel.E, units.energy.meV)
        return self.factory.constantEnergyTransferKernel(E, abs, sctt)


    def onConstantQEKernel(self, kernel):
        t = kernel

        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            abs, sctt, inc, coh = self._getXS(kernel)
            pass
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        Q = self._unitsRemover.remove_unit(kernel.Q, 1./units.length.angstrom)
        E = self._unitsRemover.remove_unit(kernel.E, units.energy.meV)
        return self.factory.constantQEKernel(Q, E, abs, sctt)


    def onConstantvQEKernel(self, kernel):
        t = kernel

        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            abs, sctt, inc, coh = self._getXS(kernel)
            pass
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )
        Q = kernel.Q
        E = self._unitsRemover.remove_unit(kernel.E, units.energy.meV)
        dE = self._unitsRemover.remove_unit(kernel.dE, units.energy.meV)
        return self.factory.constantvQEKernel(Q, E, dE, abs, sctt)


    def onE_Q_Kernel(self, kernel):
        t = kernel

        # cross section related
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections(origin, include_density=True)
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit(
            (abs, sctt), 1./units.length.meter )
        
        # functors
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q

        # Q range
        Qmin = self._unitsRemover.remove_unit(
            kernel.Qmin, 1./units.length.angstrom)
        Qmax = self._unitsRemover.remove_unit(
            kernel.Qmax, 1./units.length.angstrom)
        
        return self.factory.E_Q_Kernel(E_Q, S_Q, Qmin, Qmax, abs, sctt)


    def onBroadened_E_Q_Kernel(self, kernel):
        t = kernel

        # cross section related
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient
        
        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections(origin, include_density=True)
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit(
            (abs, sctt), 1./units.length.meter )
        
        # functors for S(Q,E)
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q
        sigma_Q = kernel.sigma_Q

        # Q range
        Qmin = self._unitsRemover.remove_unit(
            kernel.Qmin, 1./units.length.angstrom)
        Qmax = self._unitsRemover.remove_unit(
            kernel.Qmax, 1./units.length.angstrom)
        
        return self.factory.Broadened_E_Q_Kernel(
            E_Q, S_Q, sigma_Q, Qmin, Qmax, abs, sctt)


    def onLorentzianBroadened_E_Q_Kernel(self, kernel):
        t = kernel

        # cross section related
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient
        if abs is None or sctt is None:
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections(origin, include_density=True)
            sctt = inc + coh
            pass
        abs, sctt = self._unitsRemover.remove_unit(
            (abs, sctt), 1./units.length.meter )
        # functors for S(Q,E)
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q
        gamma_Q = kernel.gamma_Q

        # Q range
        Qmin = self._unitsRemover.remove_unit(
            kernel.Qmin, 1./units.length.angstrom)
        Qmax = self._unitsRemover.remove_unit(
            kernel.Qmax, 1./units.length.angstrom)
        return self.factory.LorentzianBroadened_E_Q_Kernel(
            E_Q, S_Q, gamma_Q, Qmin, Qmax, abs, sctt)


    def onE_vQ_Kernel(self, kernel):
        t = kernel

        # cross section related
        abs = t.absorption_coefficient
        sctt = t.scattering_coefficient

        if abs is None or sctt is None:
            #need to get cross section from sample assembly representation
            # svn://danse.us/inelastic/sample/.../sampleassembly
            #origin is a node in the sample assembly representation
            #
            #scatterer_origin is assigned to kernel when a kernel is
            #constructed from kernel xml.
            #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
            origin = t.scatterer_origin
            from sampleassembly import cross_sections
            abs, inc, coh = cross_sections(origin, include_density=True)
            sctt = inc + coh
            pass
        
        abs, sctt = self._unitsRemover.remove_unit( (abs, sctt), 1./units.length.meter )

        # functors
        E_Q = kernel.E_Q
        S_Q = kernel.S_Q

        # Emax
        Emax = self._unitsRemover.remove_unit(
            kernel.Emax, units.energy.meV)
        
        return self.factory.E_vQ_Kernel(E_Q, S_Q, Emax, abs, sctt)


    def onKernelContainer(self, kernelcontainer):
        #each kernel needs to know its scatterer origin.
        for kernel in kernelcontainer.elements():
            kernel.scatterer_origin = kernel
            continue
        return self.onCompositeKernel( kernelcontainer )
    
    
    def _getXS(self, kernel, include_density=False):
        t = kernel
        #need to get cross section from sample assembly representation
        # svn://danse.us/inelastic/sample/.../sampleassembly
        #origin is a node in the sample assembly representation
        #
        #scatterer_origin is assigned to kernel when a kernel is
        #constructed from kernel xml.
        #see sampleassembly_support.SampleAssembly2CompositeScatterer for details.
        origin = t.scatterer_origin
        from sampleassembly import compute_absorption_and_scattering_coeffs
        abs, inc, coh = compute_absorption_and_scattering_coeffs( origin )
        sctt = inc + coh
        return abs, sctt, inc, coh

    pass # end of ComputationEngineRendererExtension


def register( type, renderer_handler_method, override = False ):
    '''register computing engine constructor method for a new type'''

    Renderer = ComputationEngineRendererExtension
    global _registry

    name = type.__name__
    methodname = 'on%s' % name
    if hasattr(Renderer, methodname):
        if not override:
            raise ValueError("Cannot register handler for type %s"\
                  "%s already registered as handler for type %s" % (
                type, methodname, _registry[name] ))
        pass
    
    setattr( Renderer, methodname, renderer_handler_method )

    _registry[ name ] = type
    return
_registry = {}



from mccomponents.homogeneous_scatterer import registerRendererExtension
registerRendererExtension( ComputationEngineRendererExtension )


from . import units


# End of file 
