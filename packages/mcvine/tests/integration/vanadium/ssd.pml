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
        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/V_sample</facility>
        <facility name="detector">monitors/PSD_monitor_4PI</facility>

        <property name="multiple-scattering">False</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">1000</property>

        <component name="source">
            <property name="dist">9.5</property>
            <property name="height">0.1</property>
            <property name="width">0.1</property>
            <property name="xw">0.05</property>
            <property name="yh">0.05</property>
            <property name="radius">0.0</property>
            <property name="E0">60.0</property>
            <property name="dE">10.0</property>
            <property name="Lambda0">0.0</property>
            <property name="dLambda">0.0</property>
            <property name="gauss">0.0</property>
            <property name="flux">1.0</property>
        </component>


        <component name="sample">
            <property name="radius_i">0.001</property>
            <property name="radius_o">0.01</property>
            <property name="h">0.05</property>

            <property name="xwidth">0.0</property>
            <property name="yheight">0.0</property>
            <property name="zthick">0.0</property>

            <property name="focus_r">0.0</property>
            <property name="focus_xw">0.0</property>
            <property name="focus_ah">0.0</property>
            <property name="focus_aw">0.0</property>
            <property name="focus_yh">0.0</property>

            <property name="V0">13.827</property>
            <property name="sig_i">4.935</property>
            <property name="f_QE">0.0</property>
            <property name="frac">1.0</property>
            <property name="sig_a">5.08</property>
            <property name="gamma">0.0</property>
            <property name="pack">1.0</property>

            <property name="target_z">0.235</property>
            <property name="target_x">0.0</property>
            <property name="target_y">0.0</property>

        </component>


        <component name="detector">
            <property name="name">psd_monitor_4pi</property>
            <property name="filename">psd4pi.dat</property>
            <property name="nx">90.0</property>
            <property name="ny">90.0</property>
            <property name="radius">3.0</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 10), (0, 0, 0))</property>
            <property name="detector">((0, 0, 10), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->

