<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="s">
        <property name="dump-instrument">False</property>
        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>
        <property name="launcher">mpirun</property>
        <property name="sequence">['source']</property>
        <property name="ncount">10000.0</property>
        <property name="multiple-scattering">False</property>
        <facility name="source">sources/SNS_source_tf</facility>
        <facility name="geometer">geometer</facility>
        <property name="dump-registry">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="source">
            <property name="yh">0.12</property>
            <property name="dist">2.5</property>
            <property name="name">sns_source_tf</property>
            <property name="Emin">32.0</property>
            <property name="Emax">81.0</property>
            <property name="E0">40.0</property>
            <property name="t0">20</property>
            <property name="S_filename">/home/lj7/dv/mcvine/resources/instruments/ARCS/moderator/source_sct521_bu_17_1.dat</property>
            <property name="height">0.12</property>
            <property name="width">0.1</property>
            <property name="fcdist">11.61</property>
            <property name="angling">0.0</property>
            <property name="xw">0.1</property>
            <property name="logging">1</property>
        </component>


        <component name="mpirun">
            <property name="dry">False</property>
            <property name="nodelist">[]</property>
            <property name="extra"></property>
            <property name="python-mpi">`which python`</property>
            <property name="command">mpirun</property>
            <property name="debug">False</property>
            <property name="nodes-opt">-np</property>
            <property name="nodes">0</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Thu Jun 23 09:38:37 2016-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ s -mode=worker -dump-pml -source=SNS_source_tf
-->

