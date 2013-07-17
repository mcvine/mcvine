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


from mccomponents.homogeneous_scatterer import scattererEngine


def samplecomponent( name, sampleassembly_xml ):
    '''samplecomponent( name, xml ) -->  sample simulation component

    name: name of the sample
    xml: xml file describing the sample assembly
    '''
    
    import mccomposite.extensions.HollowCylinder
    import os
    filename = os.path.realpath( sampleassembly_xml )
    dir, filename = os.path.split( os.path.abspath( filename ) )
    save = os.path.abspath( os.curdir )
    os.chdir( dir )
    
    from sampleassembly.saxml import parse_file
    sa = parse_file( filename )

    from sampleassembly_support import sampleassembly2compositescatterer, \
         findkernelsfromxmls

    scatterercomposite = findkernelsfromxmls(
        sampleassembly2compositescatterer( sa ) )

    os.chdir(save)

    import mccomponents.homogeneous_scatterer as hs
    engine = hs.scattererEngine( scatterercomposite )

    engine.name = name

    return engine


def gridsqe(*args, **kwds):
    from GridSQE import GridSQE
    return GridSQE( *args, **kwds )


def sqeFromExpression(*args, **kwds):
    from SQE_fromexpression import SQE_fromexpression
    return SQE_fromexpression( *args, **kwds )


def sqekernel(*args, **kwds):
    from SQEkernel import SQEkernel
    return SQEkernel( *args, **kwds )


def isotropickernel(*args, **kwds):
    from IsotropicKernel import IsotropicKernel
    return IsotropicKernel(*args, **kwds)


def constantEnergyTransferKernel(*args, **kwds):
    from ConstantEnergyTransferKernel import ConstantEnergyTransferKernel
    return ConstantEnergyTransferKernel(*args, **kwds)


def constantQEKernel(*args, **kwds):
    from ConstantQEKernel import ConstantQEKernel
    return ConstantQEKernel(*args, **kwds)


def make_E_Q_Kernel(*args, **kwds):
    from E_Q_Kernel import E_Q_Kernel as factory
    return factory(*args, **kwds)


def broadened_E_Q_Kernel(*args, **kwds):
    from Broadened_E_Q_Kernel import Broadened_E_Q_Kernel
    return Broadened_E_Q_Kernel(*args, **kwds)


def make_E_vQ_Kernel(*args, **kwds):
    from E_vQ_Kernel import E_vQ_Kernel as factory
    return factory(*args, **kwds)


def kernelcontainer(*args, **kwds):
    from KernelContainer import KernelContainer
    return KernelContainer( *args, **kwds )



#make renderer extension available
import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    import bindings
    return

_import_bindings()


#make additional kernels available
def _import_kernels():
    try:
        import phonon.xml
        import diffraction.xml
    except ImportError as e:
        import warnings
        s = "kernels not available: phonon, diffraction:\n%s: %s" % (
            type(e), e)
        warnings.warn(s)
    return
_import_kernels()


# version
__id__ = "$Id$"

# End of file 
