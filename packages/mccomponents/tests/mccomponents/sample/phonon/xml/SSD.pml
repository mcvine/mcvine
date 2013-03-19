<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                      (C) 2006-2010  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="SSD">
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <property name="overwrite-datafiles">False</property>
        <property name="sequence">['source', 'sample', 'detector']</property>
        <property name="output-dir">out</property>
        <property name="ncount">10000.0</property>
        <property name="multiple-scattering">False</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">1000</property>
        <facility name="detector">monitors/IQE_monitor</facility>
        <property name="dump-registry">False</property>

        <component name="sample">
            <property name="xml"></property>
        </component>


        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">0.0</property>
            <property name="velocity">[0.0, 0.0, 3388.034]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="detector">
            <property name="max_angle_in_plane">120.0</property>
            <property name="Ei">60.0</property>
            <property name="name">iqe_monitor</property>
            <property name="min_angle_in_plane">0.0</property>
            <property name="Emax">45.0</property>
            <property name="Emin">-45.0</property>
            <property name="Qmax">10.0</property>
            <property name="min_angle_out_of_plane">-30.0</property>
            <property name="nE">90</property>
            <property name="Qmin">0.0</property>
            <property name="max_angle_out_of_plane">30.0</property>
            <property name="nQ">100</property>
            <property name="filename">iqe_monitor.dat</property>
        </component>


        <component name="geometer">
            <property name="sample">((0, 0, 0), (0, 0, 0))</property>
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="detector">((0, 0, 0), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Tue Oct  5 16:04:53 2010-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ SSD.py -source=MonochromaticSource -sample=SampleAssemblyFromXml -detector=IQE_monitor -h -dump-pml=yes
-->

