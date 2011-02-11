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

    <component name="testmpi">
        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="monitor">monitors/NDMonitor(energy)</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">0</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out-testmpi</property>

        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="energy">60.0</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="monitor">
            <property name="energymin">0.0</property>
            <property name="energymax">100.0</property>
            <property name="filename">ienergy.h5</property>
            <property name="nenergy">10</property>
            <property name="title">I(E)</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="monitor">((0, 0, 1), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>


    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Wed Jan 26 19:24:00 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ testmpi -h -dump-pml=yes -source=MonochromaticSource -monitor=NDMonitor(energy)
-->

