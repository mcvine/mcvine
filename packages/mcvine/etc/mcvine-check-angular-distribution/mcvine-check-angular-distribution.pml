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

    <component name="mcvine-check-angular-distribution">

        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/NeutronFromStorage</facility>
        <facility name="monitor">monitors/PSD_monitor_4PI</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">1e4</property>
        <property name="buffer_size">10000</property>

        <property name="output-dir">out-check-angular-distribution</property>
        <property name="overwrite-datafiles">True</property>

        <component name="source">
            <property name="path">neutrons</property>
        </component>

        <component name="monitor">
            <property name="radius">3</property>
            <property name="nx">100</property>
            <property name="ny">100</property>
            <property name="filename">angular-dist.dat</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="monitor">((0, 0, 0), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->

