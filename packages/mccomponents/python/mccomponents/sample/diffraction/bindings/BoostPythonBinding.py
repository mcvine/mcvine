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
import mcni.mcnibp as b2


import numpy



class New:

    def singlecrystaldiffractionkernel(
            self, basis_vectors, hkllist,
            mosaic, delta_d_d, abs_xs
    ):
        """
        avec, bvec, cvec: basis vectors
        hkllist: list of (h,k,l, F^2)
        """
        avec, bvec, cvec = basis_vectors
        a = b2.Vector3_double(*avec)
        b = b2.Vector3_double(*bvec)
        c = b2.Vector3_double(*cvec)
        lattice = b.Lattice(a,b,c)
        ra = np.array(lattice.ra)
        rb = np.array(lattice.rb)
        rc = np.array(lattice.rc)
        tosort = []
        for h,k,l,F2 in hkllist:
            q = h*ra + k*rb + l*rc
            tosort.append((np.linalg.norm(q), (h,k,l,F2)))
            continue
        tosort = sorted(tosort)
        hkllist2 = b.vector_HKL(0)
        for _, (h,k,l,F2) in tosort:
            hkl = mccomponentsbp.HKL(h,k,l, F2)
            hkllist2.append(hkl)
            continue
        bkernel = b.SimplePowderDiffractionKernel(
            lattice, hkllist2, mosaic, delta_d_d, abs_xs
        )
        return bkernel

     def simplepowderdiffractionkernel(self, data):
        "data should be an instance of class ..SimplePowderDiffractionKernel.Data"
        bdata = b.SimplePowderDiffractionData()
        props = [
            'Dd_over_d', 'DebyeWaller_factor',
            'density', 'atomic_weight',
            'unitcell_volume', 'number_of_atoms',
            'absorption_cross_section',
            'incoherent_cross_section', 'coherent_cross_section',
            ]
        for prop in props:
            val = getattr(data, prop)
            print(val)
            setattr(bdata, prop, val)
            continue

        for peak in data.peaks:
            bpeak = self.simplepowderdiffractionpeak(peak)
            bdata.peaks.append(bpeak)
            continue
    
        bkernel = b.SimplePowderDiffractionKernel(bdata)
        return bkernel
    

    def simplepowderdiffractionpeak(self, peak):
        "peak should be an instance of ..SimplePowderDiffractionKernel.Peak"
        bpeak = b.SimplePowderDiffractionData_Peak()
        props = [
            'q', 'F_squared', 'multiplicity', 
            'intrinsic_line_width', 'DebyeWaller_factor',
            ]
        for prop in props:
            val = getattr(peak, prop)
            setattr(bpeak, prop, val)
            continue
        return bpeak
    
    
    pass # end of BoostPythonBinding



extend( New )


# version
__id__ = "$Id$"

# End of file 
