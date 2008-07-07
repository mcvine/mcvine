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

    <component name="E_monitor_TestCase">

        <property name="output-dir">E_monitor_TestCase-out</property>
        <property name="sequence">['source', 'monitor']</property>
        <property name="ncount">10</property>
        <property name="buffer_size">5</property>
        <facility name="source">source</facility>
        <property name="overwrite-datafiles">1</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">10</property>
        <facility name="monitor">monitor</facility>

        <component name="source">
            <property name="yh">0.1</property>
            <property name="dist">10.0</property>
            <property name="width">0.0</property>
            <property name="dE">10.0</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.02</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">60.0</property>
            <property name="xw">0.1</property>
        </component>


        <component name="monitor">
            <property name="ymax">0.0</property>
            <property name="Emin">10.0</property>
            <property name="Emax">100.0</property>
            <property name="filename">IE.dat</property>
            <property name="nchan">20</property>
            <property name="xmax">0.0</property>
            <property name="xmin">0.0</property>
            <property name="ymin">0.0</property>
        </component>


        <component name="geometer">
            <property name="monitor">(0,0,10),(0,0,0)</property>
            <property name="source">(0,0,0),(0,0,0)</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Mon Feb  4 17:25:06 2008-->

<!-- End of file -->
