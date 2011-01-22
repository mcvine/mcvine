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
! Testing Monitor_4PI
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!-- [Source_simple] -> [V_sample] -> [Monitor_4PI] -->


<!DOCTYPE inventory>

<inventory>

    <component name="ssd1">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/V_sample</facility>
        <facility name="detector">monitors/Monitor_4PI</facility>

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
            <property name="target_index">0</property>
            <property name="radius_i">0.015</property>
            <property name="radius_o">0.02</property>
            <property name="focus_aw">0</property>
            <property name="focus_yh">1.30</property>
            <property name="V0">13.827</property>
            <property name="zthick">0</property>
            <property name="focus_ah">0</property>
            <property name="sig_i">4.935</property>
            <property name="f_QE">0</property>
            <property name="frac">1</property>
            <property name="sig_a">5.08</property>
            <property name="target_z">0</property>
            <property name="target_x">-2</property>
            <property name="target_y">0</property>
            <property name="focus_r">0</property>
            <property name="h">0.05</property>
            <property name="yheight">0</property>
            <property name="focus_xw">0.780</property>
            <property name="xwidth">0</property>
            <property name="gamma">0</property>
            <property name="pack">1</property>
        </component>

        <component name="detector">
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 2), (0, 0, 0))</property>
            <property name="detector">((0, 0, 3), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>


