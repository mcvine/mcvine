.. _SampleAssembly:

Sample Assembly
---------------

.. note::
   Several tutorials:
   
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

    </SampleAssembly>


* The outmost tag is always "SampleAssembly".
 * The next level consists of one or more neutron scatterers and one geometer.
 * PowderSample is a neutron scatterer. Its name is important (see :ref:`scatterer-xml`).
  * Inside a neutron scatterer we need to specify its shape and material
  * Shape -- can be represented using constructive solid geometery
  * Phase
 * LocalGeometer is geometer. It contains geometrical information of neutron scatterers


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
 * Inside a scatterer tag, there is one kernel tag. See :ref:`types of kernels <kernel-types>`.


.. _kernel-types:

Kernels
-------



