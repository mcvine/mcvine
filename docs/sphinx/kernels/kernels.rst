.. _kernels:

Kernels
=======

.. note::
   Developers: please also read :ref:`Kernel implementation <kernel-implementation>`.


.. _kernel_isotropic:

Isotropic
^^^^^^^^^
This kernel elastically and isotropically scatters neutrons
to all 4pi solid angle.

Parameters: None

Example::

 <IsotropicKernel/>

You can find a full example in directory "kernels/isotropic" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot (a mostly uniform distribution of 
intensities in 4pi solid angle):

.. figure:: images/kernels/isotropickernel-psd4pimonitor.png
   :width: 50%


.. _kernel_constant-energy-transfer:

Constant energy transfer
^^^^^^^^^^^^^^^^^^^^^^^^
This kernel scatters neutrons with a constant energy
transfer

.. math:: E_{f} = E_{i} - E_{constant}
   	  
The scattered neutrons goes
to all 4pi solid angle isotropically.

This kernel is mostly for testing purpose and resolution study.

Parameters: 

- energy-transfer: The energy transfer.

Example::

 <ConstantEnergyTransferKernel energy-transfer="10*meV"/>


You can find a full example in directory "kernels/constant-energy-transfer" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot:

.. figure:: images/kernels/constant-energy-transfer-kernel-iqe.png
   :width: 50%


.. _kernel_constant-qe:

Constant Q,E
^^^^^^^^^^^^
This kernel scatters neutrons with constant energy
transfer and constant momentum transfer (magnitude)

.. math:: E_{f} = E_{i} - E_{constant}
.. math:: \vec{Q}_{f} = \vec{Q}_{i} - \vec{Q}

where 

.. math:: |\vec{Q}| = Q_{constant}
   	  
This kernel is mostly for testing purpose and resolution study.

Parameters: 

- energy-transfer: The energy transfer
- momentum-transfer: The momentum transfer

Example::

  <ConstantQEKernel momentum-transfer="3/angstrom" energy-transfer="30*meV"/>

You can find a full example in directory "kernels/constant-qe-transfer" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot:

.. figure:: images/kernels/constant-qe-transfer-kernel-iqe.png
   :width: 50%



.. _kernel_sqe:

S(Q,E)
^^^^^^
This kernel scatters neutrons according to a :math:`S(|\vec{Q}|,E)` input.

Parameters: 

- Q-range: The momentum transfer range
- energy-transfer: The energy transfer range

Elements:

- GridSQE

Example::

  <SQEkernel Q-range='0*angstrom**-1,12.*angstrom**-1' energy-range='-48*meV,48*meV'>
    <GridSQE histogram-hdf-path="sqehist.h5/S(Q,E)" auto-normalization="1" />
  </SQEkernel>

You can find a full example in directory "kernels/sqe" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot:

.. figure:: images/kernels/iqekernel-iqemonitor.png
   :width: 50%

The input for this simulation is an artifical I(Q,E):

.. figure:: images/kernels/iqekernel-iqeinput.png
   :width: 50%


.. .. _kernel_sq:

.. S(Q)
.. ^^^^


.. _kernel_simplepowderdiffr:

Simple powder diffraction (experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for powder diffraction.

Parameters: 

- Dd_over_d
- DebyeWaller_factor
- peaks-py-path

Example::

  <SimplePowderDiffractionKernel Dd_over_d="1e-5" DebyeWaller_factor="1." peaks-py-path="peaks.py"/>

You can find a full example in directory "kernels/simple-powder-diffraction" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot:

.. figure:: images/kernels/simplepowderdiffraction-kernel-psd4pi.png
   :width: 50%



.. _kernel_incoh_inel_phonon_polyxtal:

Incoherent inelastic phonon scattering for polycrystal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for incoherent inelastic phonon scattering for polycrystalline sample.

Parameters: 

- average_mass: average mass of atoms in unit cell
- scattering_xs: total scattering cross section of a unit cell
- absorption_xs: total absorption cross section of a unit cell

Elements:

- LinearlyInterpolatedDOS

Example::

  <Phonon_IncoherentInelastic_Kernel>
    <LinearlyInterpolatedDOS idf-data-path="phonon-dispersion/DOS"/> 
  </Phonon_IncoherentInelastic_Kernel>

DOS data can be in different formats:

- idf-data-path
- ascii-path
- histogram-path

You could compute phonon DOS from a bvk model
using the VNF service: https://vnf.caltech.edu


.. _kernel_coh_inel_phonon_polyxtal:

Coherent inelastic phonon scattering for polycrystal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for coherent inelastic phonon scattering for polycrystalline sample.

Parameters: 

- Ei: nominal incident energy
- max-omega: maximum energy transfer
- max-Q: maximum momentum transfer

Elements:

- LinearlyInterpolatedDispersion

Example::

  <Phonon_CoherentInelastic_PolyXtal_Kernel Ei='70*meV' max-omega='55*meV' max-Q='12*angstrom**-1' nMCsteps_to_calc_RARV='10000' >
    <LinearlyInterpolatedDispersion idf-data-path="phonon-dispersion"/>
  </Phonon_CoherentInelastic_PolyXtal_Kernel>

You can find a full example in directory "kernels/phonon-coherent-inelastic-polyxtal" in
`the examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_

Running it will generate the following plot:

.. figure:: images/kernels/coh-inel-phonon-polyxtal-kernel-iqe.png
   :width: 50%

You could compute phonon dispersion from a bvk model
using the VNF service: https://vnf.caltech.edu


.. _kernel_coh_inel_phonon_singlextal:

Coherent inelastic phonon scattering for single crysal (experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


