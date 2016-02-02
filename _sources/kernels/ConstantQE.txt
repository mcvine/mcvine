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



