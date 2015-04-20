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

    <component name="ssd">
        <property name="sequence">['source', 'sample', 'detector']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">monitors/PSD_monitor_4PI</facility>

        <property name="multiple-scattering">False</property>

        <property name="overwrite-datafiles">on</property>
        <property name="output-dir">out</property>

        <property name="ncount">1e6</property>


        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="energy">0.0</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>

        <component name="sample">
            <property name="xml">sampleassembly/sampleassembly.xml</property>
        </component>

        <component name="detector">
            <property name="name">psd_monitor_4pi</property>
            <property name="restore_neutron">False</property>
            <property name="filename">psd4pi.dat</property>
            <property name="nx">90.0</property>
            <property name="ny">90.0</property>
            <property name="radius">10.0</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 1), (0, 0, 0))</property>
            <property name="detector">((0, 0, 1), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Tue Mar  8 14:51:08 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ ssd -detector=PSD_monitor_4PI -dump-pml
-->

