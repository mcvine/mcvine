<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                        (C) 2008  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->


<!DOCTYPE inventory>

<inventory>

  <component name="SSSD">

    <property name="ncount">10000</property>
    <property name="buffer_size">10000</property>
<!--
    <property name='overwrite-datafiles'>yes</property>
-->

    <component name="geometer">
      <property name="source">(0,0,0), (0,0,0)</property>
      <property name="sample">(0,0,10), (0,0,0)</property>
      <property name="neutron_storage">(0,0,10), (0,0,0)</property>
      <property name="detector">(0,0,10), (0,0,0)</property>
    </component>

    <component name="source">
      <property name="velocity">0,0,3659.51</property>
      <property name="probability">1</property>
    </component>

    <facility name="sample">fccNi_sample</facility>
    <component name="fccNi_sample">
      <property name="xml">fccNi-plate-sampleassembly.xml</property>
    </component>

    <component name="neutron_storage">
      <property name="path">neutrons</property>
    </component>

    <facility name="detector">iqe_monitor</facility>
    <component name="iqe_monitor">
      <property name='max_angle_out_of_plane'>90</property>
      <property name='min_angle_out_of_plane'>-90</property>
      <property name='max_angle_in_plane'>180</property>
      <property name='min_angle_in_plane'>-180</property>

      <property name='filename'>IQE.dat</property>

      <property name="Ei">70</property>

      <property name="Qmin">0</property>
      <property name="Qmax">11</property>
      <property name="nQ">110</property>

      <property name="Emin">-60</property>
      <property name="Emax">60</property>
      <property name="nE">120</property>
    </component>

  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by XMLMill on Mon Jul 14 13:47:59 2008-->

<!-- End of file -->
