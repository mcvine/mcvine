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


