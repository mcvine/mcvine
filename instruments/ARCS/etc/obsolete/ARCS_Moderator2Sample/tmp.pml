<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                      (C) 2005-2008 All Rights Reserved 
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->


<!DOCTYPE inventory>

<inventory>

  <component name="arcs_instr">

    <component name="moderator">
      <property name="position">(0,0,0) absolute</property>      
      <property name="rotation">(0,0,0) absolute</property>      
      <property name="S_filename">source_sct521_bu_17_1.dat</property>
      <property name="width"> 0.1 </property>
      <property name="height"> 0.12 </property>
      <property name="dist"> 2.5 </property>
      <property name="xw"> 0.1 </property>
      <property name="yh"> 0.12 </property>
    </component>

    <component name="core_vessel_insert">
      <property name="position">(0,0,1.000) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 1.252 </property>
      <property name="w1"> 0.08900 </property>
      <property name="w2"> 0.07493 </property>
      <property name="h1"> 0.10750 </property>
      <property name="h2"> 0.09404 </property>
      <property name="R0"> 0. </property>
      <property name="mx"> 2.5 </property>
      <property name="my"> 2.5 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>
    
    <component name="shutter_guide">
      <property name="position">(0,0,2.2679) relative moderator</property> 
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 1.853 </property>
      <property name="w1"> 0.07493 </property>
      <property name="w2"> 0.07088 </property>
      <property name="h1"> 0.09404 </property>
      <property name="h2"> 0.08688 </property>
      <property name="R0"> 0.99 </property>
      <property name="mx"> 2.5 </property>
      <property name="my"> 2.5 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="guide1">
      <!-- geometry -->
      <property name="position">(0,0,4.179) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 4.339 </property>
      <property name="w1"> 0.07088 </property>
      <property name="w2"> 0.06126 </property>
      <property name="h1"> 0.08688 </property>
      <property name="h2"> 0.06990 </property>
      <!-- physical properties -->
      <property name="R0"> 0.99 </property>
      <property name="mx"> 3.6 </property>
      <property name="my"> 3.6 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="t0_chopper">
      <property name="position">(0,0,9.000) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
    </component>
    
    <component name="guide2">
      <!-- geometry -->
      <property name="position">(0,0,9.482) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 1.996 </property>
      <property name="w1"> 0.06126 </property>
      <property name="w2"> 0.05580 </property>
      <property name="h1"> 0.06990 </property>
      <property name="h2"> 0.06025 </property>
      <!-- physical properties -->
      <property name="R0"> 0.99 </property>
      <property name="mx"> 3.6 </property>
      <property name="my"> 3.6 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="fermi_chopper">
      <property name="position">(0,0,11.600) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="w"> 0.06 </property>
      <property name="len"> 0.10 </property>
      <property name="ymax"> 0.03 </property>
      <property name="ymin"> -0.03 </property>
      <property name="nu"> 600 </property>
      <property name="delta"> 0.0 </property>
      <property name="tc"> 0.0 </property>
      <property name="bw"> 0.00035 </property>
      <property name="nchan"> 32 </property>
      <property name="blader"> 0.5801 </property>
    </component>
    
    <component name="guide3">
      <!-- geometry -->
      <property name="position">(0,0,11.815) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 0.228 </property>
      <property name="w1"> 0.05580 </property>
      <property name="w2"> 0.05506 </property>
      <property name="h1"> 0.06025 </property>
      <property name="h2"> 0.05894 </property>
      <!-- physical properties -->
      <property name="R0"> 0.99 </property>
      <property name="mx"> 3.6 </property>
      <property name="my"> 3.6 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="guide4">
      <!-- geometry -->
      <property name="position">(0,0,12.061) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 0.953 </property>
      <property name="w1"> 0.05500 </property>
      <property name="w2"> 0.05191 </property>
      <property name="h1"> 0.05884 </property>
      <property name="h2"> 0.05337 </property>
      <!-- physical properties -->
      <property name="R0"> 0.99 </property>
      <property name="mx"> 3.6 </property>
      <property name="my"> 3.6 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="guide5">
      <!-- geometry -->
      <property name="position">(0,0,13.017) relative moderator</property>      
      <property name="rotation">(0,0,0) absolute</property>
      <property name="l"> 0.383 </property>
      <property name="w1"> 0.05190 </property>
      <property name="w2"> 0.05065 </property>
      <property name="h1"> 0.05335 </property>
      <property name="h2"> 0.05115 </property>
      <!-- physical properties -->
      <property name="R0"> 0.99 </property>
      <property name="mx"> 3.6 </property>
      <property name="my"> 3.6 </property>
      <property name="Qcx"> 0.02 </property>
      <property name="Qcy"> 0.02 </property>
      <property name="W"> 2e-3 </property>
      <property name="alphax"> 5.5 </property>
      <property name="alphay"> 5.5 </property>
      <property name="d"> 0 </property>
      <property name="k"> 1 </property>
    </component>

    <component name="energyMonitor1">
      <property name="position">(0,0,0.390) relative guide5</property>
      <property name="rotation">(0,0,0) absolute</property>
      <property name="xmin"> -0.5 </property>
      <property name="xmax">  0.5 </property>
      <property name="ymin"> -0.5 </property>
      <property name="ymax">  0.5 </property>
      <property name="nchan"> 50 </property>
      <property name="filename">energyMonitor1.dat</property>
    </component>

    <component name="tofMonitor1">
      <property name="position">(0,0,0.390) relative guide5</property>
      <property name="rotation">(0,0,0) absolute</property>
      <property name="xmin"> -0.5 </property>
      <property name="xmax">  0.5 </property>
      <property name="ymin"> -0.5 </property>
      <property name="ymax">  0.5 </property>
      <property name="nchan"> 50 </property>
      <property name="filename">tofMonitor1.dat</property>
    </component>

  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- End of file -->
