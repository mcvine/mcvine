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

    <component name="test1">
        <property name="typos">strict</property>
        <property name="help-persistence">False</property>
        <property name="help">False</property>
        <property name="output-dir">out</property>
        <property name="sequence">['source', 'monitor']</property>
        <property name="ncount">10</property>
        <facility name="source">source</facility>
        <property name="help-properties">False</property>
        <property name="help-components">False</property>
        <property name="overwrite-datafiles">False</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">10</property>
        <facility name="monitor">monitor</facility>

        <component name="source">
            <property name="yh">0.1</property>
            <property name="help-persistence">False</property>
            <property name="dist">10.0</property>
            <property name="help">False</property>
            <property name="width">0.0</property>
            <property name="dE">10.0</property>
            <property name="help-properties">False</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.02</property>
            <property name="help-components">False</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">60.0</property>
            <property name="xw">0.1</property>
        </component>


        <component name="monitor">
            <property name="help-persistence">False</property>
            <property name="ymax">0.0</property>
            <property name="Emin">10.0</property>
            <property name="Emax">100.0</property>
            <property name="yheight">0.2</property>
            <property name="filename">IE.dat</property>
            <property name="help-properties">False</property>
            <property name="nchan">20</property>
            <property name="help-components">False</property>
            <property name="xmax">0.0</property>
            <property name="xmin">0.0</property>
            <property name="xwidth">0.2</property>
            <property name="ymin">0.0</property>
            <property name="help">False</property>
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
