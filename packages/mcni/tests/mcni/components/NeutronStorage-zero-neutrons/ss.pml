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

    <component name="ss">
        <property name="dump-instrument">False</property>
        <property name="overwrite-datafiles">False</property>
        <property name="sequence">['source', 'storage']</property>
        <property name="launcher">mpirun</property>
        <property name="post-processing-scripts-dir">/tmp/tmp9XMChx/post-processing-scripts</property>
        <property name="output-dir">out</property>
        <facility name="storage">monitors/NeutronToStorage</facility>
        <property name="ncount">10000.0</property>
        <property name="multiple-scattering">False</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="geometer">geometer</facility>
        <property name="dump-registry">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="source">
            <property name="probability">-1.0</property>
            <property name="energy">0.0</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="height">0.0</property>
            <property name="width">0.0</property>
            <property name="energy-width">0.0</property>
            <property name="time">0.0</property>
            <property name="position">[0.0, 0.0, 0.0]</property>
        </component>


        <component name="storage">
            <property name="path">neutrons</property>
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
            <property name="storage">((0, 0, 0), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Tue Jul 18 14:20:30 2017-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ simapp.py -source=MonochromaticSource -storage=NeutronToStorage -h -dump-pml -post-processing-scripts-dir=/tmp/tmp9XMChx/post-processing-scripts
-->

