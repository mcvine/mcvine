.. _SampleAssembly:

Sample Assembly
---------------

.. note::
   `The examples tar ball <http://dev.danse.us/packages/mcvine-examples.tgz>`_
   contains several examples introduced here.

.. note::
   Tutorials:
   
   * :ref:`Start from here <tutorials-sampleassembly>`
   * :ref:`Sample with powder diffraction kernel <tutorials-powder-kernel>`

Use sample assembly in your simulation application
==================================================
The component type for sample assembly is "SampleAssemblyFromXml"::

 --sample=SampleAssemblyFromXml

The only parameter for this component is the path to the xml file::

 --sample.xml=<xmlfilepath>



Files
=====

A sample assembly consists of several files.

* :ref:`The main xml file <sampleassembly-main-xml>`. 
  That is the file referred to by the "xml" parameter
  of the SampleAssemblyFromXml component.
* One xml file for each neutron scatterer in the sample assembly.


.. _sampleassembly-main-xml:

The main sample assembly xml file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It contains information about the shapes and materials of the neutron scatterers


Example::

    <?xml version="1.0"?>

    <!DOCTYPE SampleAssembly>

    <SampleAssembly name="Al">

      <PowderSample name="Al" type="sample">
        <Shape>
          <block width="6*cm" height="10*cm" thickness="1*cm" />
        </Shape>
        <Phase type="crystal">
          <ChemicalFormula>Al</ChemicalFormula>
          <xyzfile>Al.xyz</xyzfile>
        </Phase>
      </PowderSample>

      <LocalGeometer registry-coordinate-system="InstrumentScientist">
        <Register name="Al" position="(0,0,0)" orientation="(0,0,0)"/>
      </LocalGeometer>

      <Environment temperature="300*K"/>

    </SampleAssembly>


* The outmost tag is always "SampleAssembly".
 * The next level consists of one or more neutron scatterers and one geometer.
 * PowderSample is a neutron scatterer. Its name is important (see :ref:`scatterer-xml`).
  * Inside a neutron scatterer we need to specify its shape and material
  * Shape -- can be represented using constructive solid geometery
  * Phase
 * LocalGeometer is geometer. It contains geometrical information of neutron scatterers
 * Environment: sample environment.


.. _scatterer-xml:

Scatterer xml
^^^^^^^^^^^^^
A neutron scatterer is always assigned with a unique name inside the sample assembly xml
file. There must be one file named <scatterer-name>-scatteer.xml in the same directory
where the sample assembly xml is.

In the above example for sample assembly, there is one scatterer "Al". Therefore,
there must be
an Al-scatterer.xml file ::

    <?xml version="1.0"?>

    <!DOCTYPE scatterer>

    <!-- weights: absorption, scattering, transmission -->
    <homogeneous_scatterer mcweights="0, 1, 0">

      <SimplePowderDiffractionKernel Dd_over_d="1e-5" DebyeWaller_factor="1" peaks-py-path="peaks.py">
      </SimplePowderDiffractionKernel>

    </homogeneous_scatterer>

* A neutron scatterer xml file starts with a tag for the type of the scatterer.
  Currently the only type is "homogeneous_scatterer"
 * Inside a scatterer tag, there is one kernel tag. See :ref:`kernel documentation <kernels>`.



Constructive solid geometry
===========================

Sample shapes can be created using constructive solid geometry.

The coordinate system is described as three orthogonal directions:

* beam: follow neutron towards downstream. horizontal
* vertical: vertical. pointing up
* transversal: horizontal but perpendicular to beam

beam, transversal, and vertical forms a right-hand coordinate system.


Primitives:

* Sphere: centered at origin.
  - radius: radius of sphere
* Cylinder: centered at origin. vertical
  - radius: radius of cylinder
  - height: height of cylinder
* Block: centered at origin.
  - thickness: dimension along beam direction
  - width: dimension along transversal direction
  - height: dimension along vertical direction
* Pyramid: tip is at origin. the whole body is negative vertically
  - thickness: dimension of the base along beam direction
  - width: dimension of the base along transversal direction
  - height: dimension along vertical direction

Operations:
* Union: union of two or more shapes
* Intersection: intersection of two or more shapes
* Difference: difference of two shapes
* Translation: translate(body, beam=, transversal=, vertical=)
* Rotation: rotate(body, beam=, transversal=, vertical=, angle=)

.. _rotations:
  
Rotations
^^^^^^^^^
A rotation can be specified in three ways

* Rotation(body, vector, angle): rotate about a vector
* Rotation(body, beam=, transversal=, vertical=, angle=): similar to Rotation(body, vector, angle); the vector is specified by (beam, transversal, vertical)
* Rotation(body, euler_angles): see below on Euler angles

Euler angles
""""""""""""

The rotation or orientation is actually represented as Tait-Bryan angles (xy'z")
at the python layer, before being transformed to rotation matrix to be passed
into the c++ layer. We still call it euler_angles because that is easier to remember.

The Tait-Bryan angles (xy'z") represents three consecutive intrinsic rotations
around x, y', and z" axes.
See `its implementation <https://github.com/mcvine/mcvine/blob/48c288e9269a05304411cc62e4a6f53875df9204/packages/mcni/python/mcni/neutron_coordinates_transformers/mcstasRotations.py>`_ for details.
One thing to note is that three intrinsic rotations is equivalent to reversed
three extrinsic rotations. For our case, it would be equivalent to zyx rotations.


Misc
^^^^

A sampleassembly representation is converted to a mccomposite scatterer representation
by mccomponents.sample.sampleassembly_support.
