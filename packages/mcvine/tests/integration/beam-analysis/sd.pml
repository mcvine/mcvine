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

    <component name="sd">

        <property name="sequence">['source', 'detector']</property>
        <facility name="source">sources/NeutronFromStorage</facility>
        <facility name="detector">monitors/NDMonitor(x,y)</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>

        <component name="source">
            <property name="path">neutrons</property>
        </component>

        <component name="detector">
            <property name="filename">ixy.h5</property>
            <property name="xmax">0.05</property>
            <property name="xmin">-0.05</property>
            <property name="nx">20</property>
            <property name="ymax">0.05</property>
            <property name="ymin">-0.05</property>
            <property name="ny">20</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 13.45), (0, 0, 0))</property>
            <property name="detector">((0, 0, 13.6), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->


