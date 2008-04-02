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

  <component name='test-phonon_coherentinelastic_polyxtal_kernel'>
    <component name='detector'>
    <property name='max_angle_out_of_plane'>90</property>
    <property name='min_angle_out_of_plane'>-90</property>
    <property name='max_angle_in_plane'>180</property>
    <property name='min_angle_in_plane'>-180</property>
    <property name='filename'>IQE.dat</property>
    </component>

    <property name='overwrite-datafiles'>yes</property>
    <property name='ncount'>1e4</property>
    <property name='buffer_size'>1000</property>
  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by XMLMill on Sun Mar 30 09:25:23 2008-->

<!-- End of file -->
