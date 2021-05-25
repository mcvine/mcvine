.. _kernel_sqe:

S(Q,E)
^^^^^^
This kernel scatters neutrons according to a :math:`S(|\vec{Q}|,E)` input.

Parameters: 

- `Q-range`: The momentum transfer range
- `energy-range`: The energy transfer range

Elements:

- `GridSQE`

  * `histogram-hdf-path`: {path to the HDF5 file for SQE data}/{histogram name}

Example::

  <SQEkernel
    Q-range='0*angstrom**-1, 4.*angstrom**-1'
    energy-range='-6*meV, 6*meV'
  >
    <GridSQE histogram-hdf-path="sqehist.h5/S(Q,E)"/>
  </SQEkernel>

The `S(Q,E)` input is specified by using a HDF5 file (`sqehist.h5` in the example above)
with `S` values on a grid of `Q`, `E`.
An example input provided by Georg Ehlers for D2O coherent scattering looks like this:

.. figure:: ../images/kernels/D2O-coh-SQE.png
   :width: 50%

