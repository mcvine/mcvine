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

    <component name="ssd">
        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">False</property>
	
        <property name="ncount">10000.0</property>
        <property name="multiple-scattering">off</property>
	
        <property name="sequence">['source', 'sample', 'detector']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">monitors/IQE_monitor</facility>
	
        <property name="tracer">no-neutron-tracer</property>
	
        <component name="geometer">
            <property name="sample">((0, 0, 0), (0, 0, 0))</property>
            <property name="source">((0, 0, -1), (0, 0, 0))</property>
            <property name="detector">((0, 0, 0), (0, 0, 0))</property>
        </component>

        <component name="source">
            <property name="probability">1</property>
            <property name="width">0.0</property>
            <property name="height">0.0</property>
            <property name="energy">60.0</property>
            <property name="energy-width">0</property>
            <property name="time">0</property>
            <property name="position">0,0,0</property>
            <property name="velocity">0,0,1</property>
        </component>

        <component name="sample">
            <property name="xml">sampleassembly/sampleassembly.xml</property>
        </component>
	
        <component name="detector">
            <property name="name">iqe_monitor</property>
            <property name="Ei">60.0</property>
            <property name="min_angle_in_plane">0.0</property>
            <property name="max_angle_in_plane">120.0</property>
            <property name="min_angle_out_of_plane">-30.0</property>
            <property name="max_angle_out_of_plane">30.0</property>
            <property name="Qmin">0.0</property>
            <property name="Qmax">10.0</property>
            <property name="nQ">100</property>
            <property name="Emin">-45.0</property>
            <property name="Emax">45.0</property>
            <property name="nE">90</property>
            <property name="restore_neutron">False</property>
            <property name="filename">iqe.dat</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- 
 automatically created by the following command:
 $ ssd -source=Source_simple -sample=SampleAssemblyFromXml -detector=IQE_monitor -dump-pml
-->
<!-- End of file -->

