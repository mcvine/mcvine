#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from mccomponents.homogeneous_scatterer.bindings.BoostPythonBinding \
     import BoostPythonBinding, extend

import mcni.mcnibp as b1
import mccomposite.mccompositebp as b2
import mccomponents.mccomponentsbp as b3
import mccomponents.sansmodel_sk_bp as b4


class New:

    def sansspheremodel_kernel(self, scale, radius, contrast, background,
                           absorption_cross_section, scattering_cross_section,
                           Qmin, Qmax):
        
        spheremodel = b4.SANSModel_Sphere( scale, radius, contrast, background )
        spheresq = b4.SANSModel_Sphere_SQAdaptor( spheremodel )
        return b3.SQkernel(
            absorption_cross_section, scattering_cross_section,
            spheresq,
            Qmin, Qmax)

    pass # end of BoostPythonBinding


extend( New )


# version
__id__ = "$Id$"

# End of file 
