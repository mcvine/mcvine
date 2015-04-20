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
        <facility name="detector">monitors/IQE_monitor</facility>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out</property>

        <property name="ncount">1e6</property>
        <property name="multiple-scattering">False</property>


        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">100.0</property>
            <property name="velocity">[0.0, 0.0, 1.0]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="sample">
            <property name="xml">sampleassembly/sampleassembly.xml</property>
        </component>


        <component name="detector">
            <property name="min_angle_in_plane">-30.0</property>
            <property name="max_angle_in_plane">150.0</property>
            <property name="min_angle_out_of_plane">-80.0</property>
            <property name="max_angle_out_of_plane">80.0</property>
            <property name="Ei">100.0</property>
            <property name="Qmin">0.0</property>
            <property name="Qmax">13.0</property>
            <property name="nQ">20</property>
            <property name="Emin">-45.0</property>
            <property name="Emax">45.0</property>
            <property name="nE">30</property>
            <property name="filename">iqe.dat</property>
        </component>


        <component name="geometer">
            <property name="sample">((0, 0, 1), (0, 0, 0))</property>
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="detector">((0, 0, 1), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>


    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Fri Mar 11 16:34:43 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ ssd -detector=IQE_monitor -dump-pml
-->

