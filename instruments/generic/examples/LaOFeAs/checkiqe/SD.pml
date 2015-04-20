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

  <component name="SD">

    <property name="ncount">31800000</property>
    <property name="buffer_size">100000</property>
<!--
    <property name='overwrite-datafiles'>yes</property>
-->

    <component name="geometer">
      <property name="source">(0,0,0), (0,0,0)</property>
      <property name="detector">(0,0,0), (0,0,0)</property>
    </component>

    <facility name="source">neutrons_from_storage</facility>
    <component name="neutrons_from_storage">
      <property name="path">neutrons_scattered_by_sample</property>
    </component>

    <property name="detector">iqe_monitor</property>
    <component name="iqe_monitor">
      <property name='max_angle_out_of_plane'>90</property>
      <property name='min_angle_out_of_plane'>-90</property>
      <property name='max_angle_in_plane'>180</property>
      <property name='min_angle_in_plane'>-180</property>

      <property name='filename'>IQE.dat</property>

      <property name="Ei">70</property>

      <property name="Qmin">0</property>
      <property name="Qmax">13</property>
      <property name="nQ">130</property>

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
