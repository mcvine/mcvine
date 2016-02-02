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


