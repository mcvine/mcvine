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

    <component name="checksqe">

        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/NeutronFromStorage</facility>
        <facility name="monitor">monitors/IQE_monitor</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">1e4</property>
        <property name="buffer_size">10000</property>

        <property name="output-dir">out-check</property>
        <property name="overwrite-datafiles">True</property>

        <component name="source">
            <property name="path">neutrons</property>
        </component>

        <component name="monitor">
            <property name="Ei">80</property>
            <property name="Emin">-75</property>
            <property name="Emax">75</property>
            <property name="Qmin">0</property>
            <property name="Qmax">12</property>
            <property name="nE">150</property>
            <property name="nQ">120</property>
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

