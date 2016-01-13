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


