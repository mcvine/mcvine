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


def sqekernel(*args, **kwds):
    from SQEkernel import SQEkernel
    return SQEkernel( *args, **kwds )


def isotropickernel(*args, **kwds):
    from IsotropicKernel import IsotropicKernel
    return IsotropicKernel(*args, **kwds)


def constantEnergyTransferKernel(*args, **kwds):
    from ConstantEnergyTransferKernel import ConstantEnergyTransferKernel
    return ConstantEnergyTransferKernel(*args, **kwds)


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


# version
__id__ = "$Id$"

# End of file 
