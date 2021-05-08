.. _kernel_simplepowderdiffr:

Simple powder diffraction (experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This kernel is for powder diffraction.

Parameters: 

- `Dd_over_d`: :math:`\frac{\Delta d}{d}`
- `laz-path`: laz file for diffraction peaks
- `peaks-py-path`: python file for diffraction peaks
- `DebyeWaller_factor`: obsolete. Debye-waller factor

Example::

  <SimplePowderDiffractionKernel Dd_over_d="1e-5" peaks-py-path="peaks.py"/>

Learn how to create a powder diffraction kernel using
`the example notebook <https://github.com/mcvine/training/tree/master/sample/Al_powder-diffraction.ipynb>`_
