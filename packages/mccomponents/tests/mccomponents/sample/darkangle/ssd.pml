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

    <component name="ssd">
        <property name="overwrite-datafiles">on</property>
        <property name="multiple-scattering">False</property>
	
        <property name="sequence">['source', 'sample', 'detector']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">monitors/PSD_monitor_4PI</facility>
	
        <property name="buffer_size">1000</property>
        <property name="ncount">10000.0</property>
	
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>
	
        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">0.0</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>
	
	
        <component name="sample">
            <property name="xml">Fe-isotropickernel/sampleassembly.xml</property>
        </component>
	
	
        <component name="detector">
            <property name="nx">90.0</property>
            <property name="ny">90.0</property>
            <property name="radius">3.0</property>
            <property name="name">monitor</property>
            <property name="filename">iqemon.dat</property>
        </component>


        <component name="geometer">
            <property name="sample">((0, 0, 5), (0, 0, 0))</property>
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="detector">((0, 0, 5), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Thu Sep 23 13:59:32 2010-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ ssd -source=MonochromaticSource -sample=SampleAssemblyFromXML -detector=PSD_monitor_4PI -h -dump-pml=yes
-->

