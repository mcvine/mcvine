<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                             Alex Dementsov
!                      California Institute of Technology
!                      (C) 2006-2010  All Rights Reserved
!
! {LicenseText}
!
! Testing SampleKernel with TOF_monitor
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!-- [Source_simple] -> [SampleKernel] -> [TOF_monitor] -->

<!DOCTYPE inventory>

<inventory>

    <component name="ssd2_1">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">monitors/TOF_monitor</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">

            <property name="yh">0.1</property>
            <property name="dist">10.0</property>
            <property name="name">source_simple</property>
            <property name="width">0.0</property>
            <property name="dE">10.0</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.05</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">60.0</property>
            <property name="xw">0.1</property>

        </component>

        <component name="sample">
            <property name="xml">Al_SimplePowderDiffractionKernel/sampleassembly.xml</property>
        </component>

        <component name="detector">

            <property name="filename">tof_monitor2_1.txt</property>
            <property name="xwidth">0.05</property>
            <property name="yheight">0.05</property>
            <property name="nchan">1000</property>
            <property name="t0">1.0</property>
            <property name="t1">10000.0</property>

        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 2), (0, 0, 0))</property>
            <property name="detector">((0, 0, 3), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>


