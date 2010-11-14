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

    <component name="ss">
        <property name="sequence">['source', 'sample']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
	
        <property name="multiple-scattering">True</property>
	
        <property name="ncount">1</property>
        <property name="buffer_size">1</property>
	
        <property name="tracer">console</property>
	
        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">1</property>
	
        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">0.0</property>
            <property name="velocity">[0.0, 0.0, 4149.48]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="sample">
            <property name="xml">sampleassemblies/bmg/sampleassembly.xml</property>
        </component>
	
	
        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 1), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Sun Nov  7 08:01:20 2010-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ ss -source=MonochromaticSource -sample=SampleAssemblyFromXml -h -dump-pml
-->

