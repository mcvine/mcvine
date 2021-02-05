.. _kernel_incoh_el_phonon_polyxtal:

Incoherent Elastic scattering for polycrystal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for Incoherent Elastic scattering for  a polycrystalline sample.

Parameters: 

- dw_core: average displacement squared projected to :math:`Q` (:math:`<u^2_Q>`)
- scattering_xs: total scattering cross section of a unit cell
- absorption_xs: total absorption cross section of a unit cell

Example::

  <Phonon_IncoherentElastic_Kernel
	 dw_core="0.0073*angstrom**2" 
	 scattering_xs="3.71*barn"
	 absorption_xs="0.063*barn"
	 >
	</Phonon_IncoherentElastic_Kernel>


Explanation of "dw_core"
++++++++++++++++++++++++

Debye Waller factor is written as :math:`exp(-2W)`,
where :math:`2W = <u_Q^2> Q^2`.
The "dw_core" quantity is :math:`<u_Q^2>`,
and in case of cubic crystal,
:math:`\frac{1}{3} <u^2>`,
which can be computed from phonon DOS.

You can use command::

 $ mcvine-debye-waller-core-from-phonon-dos
 
to calculate dw_core.
Run ::

 $ mcvine-debye-waller-core-from-phonon-dos -h
 $ mcvine-debye-waller-core-from-phonon-dos --help-properties

to get help about that command
