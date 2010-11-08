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

    <component name="vulcan-ssd">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">detectorsystem</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">False</property>
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
            <property name="xml">sampleassembly.xml</property>
        </component>

        <component name="detector">
            <component name="m1">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m1.dat</property>
	    </component>
            <component name="m2">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m2.dat</property>
	    </component>
            <component name="m3">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m3.dat</property>
	    </component>
            <component name="m4">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m4.dat</property>
	    </component>
            <component name="m5">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m5.dat</property>
	    </component>
            <component name="m6">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
	      <property name="filename">m6.dat</property>
	    </component>
        </component>

        <component name="geometer">
            <property name="sample">((0, 0, 0), (0, 0, 0))</property>
            <property name="source">((0, 0, 1), (0, 0, 0))</property>
            <property name="detector">((0, 0, 2), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Sat Oct 23 04:21:06 2010-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ vulcan-ssd -h -source=Source_simple -sample=SampleAssemblyFromXml -dump-pml=yes
-->

