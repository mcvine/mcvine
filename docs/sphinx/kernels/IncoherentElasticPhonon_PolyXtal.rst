.. _kernel_incoh_el_phonon_polyxtal:

Incoherent Elastic scattering for polycrystal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for Incoherent Elastic scattering for  a polycrystalline sample.

Parameters: 

- dw_core: average displacement squared (:math:`<u^2>`)
- scattering_xs: total scattering cross section of a unit cell
- absorption_xs: total absorption cross section of a unit cell

Example::

  <Phonon_IncoherentElastic_Kernel
	 dw_core="0.0073*angstrom**2" 
	 scattering_xs="3.71*barn"
	 absorption_xs="0.063*barn"
	 >
	</Phonon_IncoherentElastic_Kernel>




