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
        <property name="dump-instrument">False</property>
        <property name="overwrite-datafiles">on</property>
        <property name="sequence">['source', 'detector']</property>
        <property name="launcher">mpirun</property>
        <property name="output-dir">out</property>
        <property name="ncount">10000.0</property>
        <property name="multiple-scattering">False</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <property name="mode">worker</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">0</property>
        <property name="detector">printer</property>
        <property name="dump-registry">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">0.0</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="mpirun">
            <property name="dry">False</property>
            <property name="nodelist">[]</property>
            <property name="extra"></property>
            <property name="python-mpi">`which python`</property>
            <property name="command">mpirun</property>
            <property name="debug">False</property>
            <property name="nodes">0</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="detector">((0, 0, 0), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Sun Feb 27 23:08:40 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ sd -detector=printer -dump-pml
-->

