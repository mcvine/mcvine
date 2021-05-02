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
    from mccomposite.extensions import HollowCylinder, SphereShell
    import os
    filename = os.path.realpath( sampleassembly_xml )
    dir, filename = os.path.split( os.path.abspath( filename ) )
    save = os.path.abspath( os.curdir )
    os.chdir( dir )
    
    from sampleassembly.saxml import parse_file
    sa = parse_file( filename )

    from .sampleassembly_support import sampleassembly2compositescatterer, \
         findkernelsfromxmls

    scatterercomposite = findkernelsfromxmls(
        sampleassembly2compositescatterer( sa ) )

    os.chdir(save)

    import mccomponents.homogeneous_scatterer as hs
    engine = hs.scattererEngine( scatterercomposite )

    engine.name = name

    return engine


def gridsqe(*args, **kwds):
    from .GridSQE import GridSQE
    return GridSQE( *args, **kwds )


def sqeFromExpression(*args, **kwds):
    from .SQE_fromexpression import SQE_fromexpression
    return SQE_fromexpression( *args, **kwds )


def sqekernel(*args, **kwds):
    from .SQEkernel import SQEkernel
    return SQEkernel( *args, **kwds )

def sqe_energyfocusing_kernel(*args, **kwds):
    from .SQE_EnergyFocusing_Kernel import SQE_EnergyFocusing_Kernel as ctor
    return ctor( *args, **kwds )


def gridsq(*args, **kwds):
    from .GridSQ import GridSQ
    return GridSQ( *args, **kwds )


def sqFromExpression(*args, **kwds):
    from .SQ_fromexpression import SQ_fromexpression
    return SQ_fromexpression( *args, **kwds )


def sqkernel(*args, **kwds):
    from .SQkernel import SQkernel
    return SQkernel( *args, **kwds )


def isotropickernel(*args, **kwds):
    from .IsotropicKernel import IsotropicKernel
    return IsotropicKernel(*args, **kwds)


def dgssxreskernel(*args, **kwds):
    from .DGSSXResKernel import DGSSXResKernel
    return DGSSXResKernel(*args, **kwds)


def constantEnergyTransferKernel(*args, **kwds):
    from .ConstantEnergyTransferKernel import ConstantEnergyTransferKernel
    return ConstantEnergyTransferKernel(*args, **kwds)


def constantQEKernel(*args, **kwds):
    from .ConstantQEKernel import ConstantQEKernel
    return ConstantQEKernel(*args, **kwds)


def constantvQEKernel(*args, **kwds):
    from .ConstantvQEKernel import ConstantvQEKernel
    return ConstantvQEKernel(*args, **kwds)


def make_E_Q_Kernel(*args, **kwds):
    from .E_Q_Kernel import E_Q_Kernel as factory
    return factory(*args, **kwds)


def broadened_E_Q_Kernel(*args, **kwds):
    from .Broadened_E_Q_Kernel import Broadened_E_Q_Kernel
    return Broadened_E_Q_Kernel(*args, **kwds)


def make_E_vQ_Kernel(*args, **kwds):
    from .E_vQ_Kernel import E_vQ_Kernel as factory
    return factory(*args, **kwds)


def kernelcontainer(*args, **kwds):
    from .KernelContainer import KernelContainer
    return KernelContainer( *args, **kwds )



#make renderer extension available
from . import ComputationEngineRendererExtension

#make bindings available
def _import_bindings():
    from . import bindings
    return

_import_bindings()


#make additional kernels available
def _import_kernels():
    try:
        from .phonon import xml
        from .diffraction import xml
    except ImportError as e:
        import warnings, traceback
        s = "kernels not available: phonon, diffraction:\n%s: %s.\n%s" % (
            type(e), e, traceback.format_exc())
        warnings.warn(s)
    return
_import_kernels()


# version
__id__ = "$Id$"

# End of file 
