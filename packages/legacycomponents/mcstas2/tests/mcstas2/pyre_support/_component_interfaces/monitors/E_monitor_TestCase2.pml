<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                        (C) 2007  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="E_monitor_TestCase2">

        <property name="output-dir">out-E_monitor_TestCase2</property>
        <property name="sequence">['source', 'monitor']</property>
        <property name="ncount">100</property>
        <property name="buffer_size">10</property>
        <property name="overwrite-datafiles">1</property>

	<facility name='source'>MonochromaticSource</facility>

        <component name="source">
            <property name="energy">60</property>
        </component>


        <component name="monitor">
            <property name="Emin">10.0</property>
            <property name="Emax">100.0</property>
            <property name="filename">IE.dat</property>
            <property name="nchan">20</property>
            <property name="xmin">-5.0</property>
            <property name="xmax">5.0</property>
            <property name="ymin">-5.0</property>
            <property name="ymax">5.0</property>
        </component>


        <component name="geometer">
            <property name="monitor">(0,0,10),(0,0,0)</property>
            <property name="source">(0,0,0),(0,0,0)</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id: E_monitor_TestCase.pml 852 2011-02-08 01:00:33Z linjiao $-->

<!-- Generated automatically by Renderer on Mon Feb  4 17:25:06 2008-->

<!-- End of file -->
