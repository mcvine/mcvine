<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                      (C) 2006-2011  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

<!--
Name: 700-0.5-AST

Description: Optimized for 700meV at 600Hz (high resolution), slats from Astrium, 1 x standard aluminum slit per slat

Rotor radius: 50mm

Slat curvature (radius): 1535mm

Slat thickness: 0.351mm

Slit thickness: 0.508mm

Number of channels: 70

Total width (w)
   w = slat_thickness * (nchan+1) + slit_thickness * nchan
   w = 0.351*71 + 0.508*70 = 60.481 mm

Blade width (bw)
   That is just the slat thickness: 0.351mm

Blade radius (blader)
    That is ths Slat radius: 1535mm
-->

        <component name="fermichopper-700-0.5-AST">
            <property name="nu">600.0</property>

            <property name="len">0.1</property>
            <property name="ymin">-0.0325</property>
            <property name="ymax">0.0325</property>
	    
            <property name="delta">0.0</property>
            <property name="tc">0.0</property>
	    
            <property name="nchan">70.0</property>
            <property name="w">0.060481</property>
            <property name="bw">0.000351</property>
            <property name="blader">1.535</property>
	    
            <property name="max_iter">10000</property>
        </component>


</inventory>
<!-- version-->
<!-- $Id: arcs_moderator2sample.pml 1067 2011-03-25 12:48:41Z linjiao $-->

<!-- End of file -->


