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

    <component name="neutron_storage_normalization_TestCase-app">

        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="monitor">monitors/NeutronToStorage</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">0</property>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out-neutron_storage_normalization_TestCase-app</property>

        <component name="source">
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="velocity">[0.0, 0.0, 3000.0]</property>
            <property name="energy">0.0</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>

        <component name="monitor">
            <property name="path">neutrons</property>
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

<!-- Generated automatically by Renderer on Wed Jan 26 15:02:36 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ neutron_storage_normalization_TestCase-app -h -dump-pml=yes -source=MonochromaticSource -monitor=NeutronToStorage
-->

