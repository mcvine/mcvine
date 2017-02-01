.. _relnotes:

Release Notes 1.2 - Feb 2016
============================

In this release, we

* Made the DGS workflow tools more generic and added the HYSPEC workflow (see `example notebooks <https://github.com/mcvine/training/tree/85942f267a085c0b4456ae177c06b5e4c804a12b/HYSPEC>`_);
* Added CLI "mcvine phonon" (see examples in `this python test case <https://github.com/mcvine/mcvine/blob/a28e6c876f52e8dcf47b9f52692159852c58138a/packages/mcvine/tests/bin/phonon/Phonon_TestCase.py>`_);
* Made simulation applications more slurm-friendly -- MPI launcher can now be customized by env var
    .. code-block:: shell

       $ export MCVINE_MPI_LAUNCHER=mpich2(mpirun)/slurm/serial
* Added a composite shape for sample specification: SphereShell (`example xml specification <https://github.com/mcvine/mcvine/blob/f09ca1b2b2a1f8e0bde080169025f9da3b64f23d/packages/mccomponents/tests/mccomponents/sample/shape-positioning/sphere-shell/sampleassembly.xml#L9>`_);
* fixed bugs.

Please refer to `related tickets <https://github.com/mcvine/mcvine/milestone/4?closed=1>`_
for more details.


Source code
-----------
can be found at `github <https://github.com/mcvine/mcvine/releases/tag/v1.2>`_


Installation
------------
The release can be :ref:`installed <installation>`
on most of recent linux distributions using conda.


Training materials
------------------
The MCViNE training materials now hosted at
`mcvine training github site <https://github.com/mcvine/training>`_.

