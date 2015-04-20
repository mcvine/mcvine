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
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <property name="dump-instrument">False</property>
        <property name="overwrite-datafiles">True</property>
        <property name="sequence">['source', 'sample', 'detector']</property>
        <property name="launcher">mpirun</property>
        <property name="output-dir">out</property>
        <property name="ncount">1000000.0</property>
        <property name="multiple-scattering">False</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <property name="mode">worker</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">0</property>
        <facility name="detector">monitors/PSD_monitor_4PI</facility>
        <property name="dump-registry">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="mpirun">
            <property name="dry">False</property>
            <property name="nodelist">[]</property>
            <property name="extra"></property>
            <property name="python-mpi">`which python`</property>
            <property name="command">mpirun</property>
            <property name="debug">False</property>
            <property name="nodes">0</property>
        </component>


        <component name="sample">
            <property name="xml">sampleassembly/sampleassembly.xml</property>
        </component>


        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">100.0</property>
            <property name="velocity">[0.0, 0.0, 1.0]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="geometer">
            <property name="sample">((0, 0, 1), (0, 0, 0))</property>
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="detector">((0, 0, 1), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>


        <component name="detector">
            <property name="restore_neutron">False</property>
            <property name="filename">psd4pi.dat</property>
            <property name="nx">180.0</property>
            <property name="ny">180.0</property>
            <property name="radius">10.0</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Tue Mar 15 16:38:26 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ ssd -detector=PSD_monitor_4PI -dump-pml
-->

