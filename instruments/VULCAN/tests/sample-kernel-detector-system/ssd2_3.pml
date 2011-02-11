<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                             Jiao Lin, Alex Dementsov
!                      California Institute of Technology
!                      (C) 2006-2010  All Rights Reserved
!
! {LicenseText}
!
! Testing PowderN component with PSD_monitor_4PI monitor
!
! Notes:
!   - This test is similar to ssd2_3.inst McStas configuration file
!   - Updated parameters for Source_simple
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!-- [Source_simple] -> [PowderN] -> [PSD_monitor_4PI] -->

<!DOCTYPE inventory>

<inventory>

    <component name="ssd2_3">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/PowderN</facility>
        <facility name="detector">monitors/PSD_monitor_4PI</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">

            <property name="yh">0.1</property>
            <property name="dist">2.0</property>
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

            <property name="reflections">Al_assembly/Al_2.laz</property>
            <property name="yheight">0.1</property>
            <property name="xwidth">0.1</property>
            <property name="zthick">0.01</property>
            <property name="DW">0</property>
            <property name="Delta_d">1e-5</property>
            <property name="frac">0</property>
            <property name="tfrac">0</property>
            
        </component>

        <component name="detector">
            <property name="filename">psd_monitor_4pi2_3.txt</property>
            <property name="nx">100</property>
            <property name="ny">100</property>
            <property name="radius">0.025</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 2), (0, 0, 0))</property>
            <property name="detector">((0, 0, 2), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>


