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

