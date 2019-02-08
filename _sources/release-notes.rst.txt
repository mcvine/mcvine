.. _relnotes:

Release Notes 1.3.2 - Feb 9th 2019
===================================

In this release, we made the following improvements

* Overall infrastructure
  
  - added support for instrument simulation without the pyre infrastructure. Some examples of using this new capability can be found in `the training notebooks <https://github.com/mcvine/training/tree/4b5f8434c776c734a594ae75a1b0b70fc81af01f/instrument_simulation>`_
  - made the histogram-merging step (after simulation) faster
  - added support for gcc 7 compiler
  - added support for boost 1.69
  - added a tool to convert mcstas instrument to non-pyre python script. :code:`$ mcvine mcstas convertinstrument`
  
* Sample assembly
      
  - kernel orientation. `Example <https://github.com/mcvine/mcvine/blob/18c24c0504050182b48918d7ee12d686f7143ec7/packages/mccomponents/tests/mccomponents/sample/kernel-orientation/kernelorientation_TestCase.py>`_
  - new shapes: pyramid and cone. See :ref:`shapes <constructive_solid_geometry>`
  - shape validation: the command :code:`$ mcvine sampleassembly check {filename}` now checks whether shapes in the sample assembly overlap
  - warn about ``max_multiplescattering_loops_among_scatterers`` parameter if not set conservatively during sampleassembly check
  - xml: support union and intersection for more than two shapes
  - xml: support spec of rotation as axis and angle. `Example <https://github.com/mcvine/mcvine/blob/0380b7e10f654b51f2b29dcfc64e54062791d641/packages/mccomponents/tests/mccomponents/sample/complex-shape/collimator/collimator_shape.xml>`_
  - added support for cif files for specification of material structure. `Example <https://github.com/mcvine/mcvine/blob/6bb175de01e911df1061c823e4723fddfd9e93e5/packages/mccomponents/tests/mccomponents/sample/sampleassemblies/B4C/sampleassembly.xml>`_
  - added a function to create diffraction peaks python file from material structure. `Example <https://github.com/mcvine/mcvine/blob/2ef5744e7a3b6f97f0093fbb3cf96feb786f25fa/packages/mccomponents/tests/mccomponents/sample/diffraction/powder_peaks_TestCase.py#L29>`_
  - support of shape specification using yaml. `Example <https://github.com/mcvine/workflow/blob/6e28719fd273a0e92b16645230f8d87dae869323/tests/data/V-plate.yml>`_
  - added a S(Q) kernel. `Example <https://github.com/mcvine/mcvine/blob/18c24c0504050182b48918d7ee12d686f7143ec7/packages/mccomponents/tests/mccomponents/sample/sampleassemblies/V-sqkernel/V-scatterer.xml>`_
  - (developer) introduced boundingbox. `BoundingBoxMaker <https://github.com/mcvine/mcvine/blob/18c24c0504050182b48918d7ee12d686f7143ec7/packages/mccomposite/lib/geometry/visitors/BoundingBoxMaker.h>`_

* Other

  - added a command to print mcvine version: :code:`$ mcvine version`
  - fixed various bugs

Please refer to `related tickets <https://github.com/mcvine/mcvine/milestone/9?closed=1>`_
for more details.


Source code
-----------
can be found at `github <https://github.com/mcvine/mcvine/releases/tag/v1.3.2>`_


Installation
------------
The release can be :ref:`installed <installation>`
on most of recent linux distributions using conda.


Training materials
------------------
The MCViNE training materials now hosted at
`mcvine training github site <https://github.com/mcvine/training>`_.
