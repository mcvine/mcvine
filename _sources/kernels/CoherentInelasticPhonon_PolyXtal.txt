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


