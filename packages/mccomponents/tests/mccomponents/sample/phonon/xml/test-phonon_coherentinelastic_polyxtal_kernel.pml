<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                        (C) 2007  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->


<!DOCTYPE inventory>

<inventory>

  <component name="test-phonon_coherentinelastic_polyxtal_kernel">

    <facility name="source">sources/MonochromaticSource</facility>
    <facility name="sample">samples/SampleAssemblyFromXml</facility>
    <facility name="detector">monitors/IQE_monitor</facility>

    <property name="overwrite-datafiles">yes</property>
    <property name="ncount">1e4</property>
    <property name="buffer_size">1000</property>

    <component name="source">
      <property name="position">[0.0, 0.0, 0.0]</property>
      <property name="energy">70.0</property>
      <property name="velocity">[0.0, 0.0, 1.0]</property>
      <property name="probability">1.0</property>
      <property name="time">0.0</property>
    </component>

    <component name="sample">
      <property name="xml">sampleassemblies/coh-inel-polyxtal/sampleassembly.xml</property>
    </component>

    <component name="detector">
      <property name="max_angle_out_of_plane">90</property>
      <property name="min_angle_out_of_plane">-90</property>
      <property name="max_angle_in_plane">180</property>
      <property name="min_angle_in_plane">-180</property>
      <property name="filename">IQE.dat</property>
      <property name="Ei">70.0</property>
      <property name="Emax">60.0</property>
      <property name="Emin">-60.0</property>
      <property name="nE">120</property>
      <property name="Qmin">0.0</property>
      <property name="Qmax">11.0</property>
      <property name="nQ">110</property>
      <property name="min_angle_out_of_plane">-30.0</property>
      <property name="max_angle_out_of_plane">30.0</property>
      <property name="filename">iqe_monitor.dat</property>
    </component>

    <component name="geometer">
      <property name="source">((0, 0, 0), (0, 0, 0))</property>
      <property name="sample">((0, 0, 10), (0, 0, 0))</property>
      <property name="detector">((0, 0, 10), (0, 0, 0))</property>
    </component>

  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- End of file -->
