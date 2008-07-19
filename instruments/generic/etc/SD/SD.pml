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

  <component name='SD'>

    <property name="overwrite-datafiles">1</property>

    <component name="geometer">
      <property name="source">(0,0,0), (0,0,0)</property>
      <property name="detector">(0,0,0), (0,0,0)</property>
    </component>

    <facility name="source">mono_source</facility>
    <component name="mono_source">
      <property name="position">0,0,0</property>
      <property name="velocity">0,0,3000</property>
      <property name="probability">1</property>
      <property name="time">0</property>
    </component>

    <facility name="detector">e_monitor</facility>
    <component name="e_monitor">
      <property name="Emin">0</property>
      <property name="Emax">100</property>
    </component>

  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by XMLMill on Fri Jul 18 18:59:40 2008-->

<!-- End of file -->
