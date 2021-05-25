.. _kernel_incoh_inel_phonon_polyxtal:

Incoherent inelastic phonon scattering for polycrystal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for incoherent inelastic phonon scattering for polycrystalline sample.

Parameters: 

- `average_mass`: (optional) average mass of atoms in unit cell. Example: `51*u`
- `scattering_xs`: (optional) total scattering cross section of a unit cell. Example: `10*barn`
- `absorption_xs`: (optional) total absorption cross section of a unit cell. Example: `5*barn`

Elements:

- `LinearlyInterpolatedDOS`

  * `idf-data-path`: path to DOS file in IDF format
  * `histogram-path`: path to DOS file in histogram HDF5 format
  * `ascii-path`: path to DOS file in ascii format.
    At least two columns. First column should be energy(meV) or frequency (teraHz). 
    Specify unit of first column in a comment line: meV or teraHz

`LinearlyInterpolatedDOS` requires a DOS data file.
Choose one of the option above to specify its path.

Example::

  <Phonon_IncoherentInelastic_Kernel>
    <LinearlyInterpolatedDOS idf-data-path="phonon-dispersion/DOS"/> 
  </Phonon_IncoherentInelastic_Kernel>

Learn how to create a powder diffraction kernel using
`the example notebook <https://nbviewer.jupyter.org/github/mcvine/training/blob/master/sample/Al_powder-IncoherentPhonon.ipynb>`_
