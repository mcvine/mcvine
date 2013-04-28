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

    <component name="sd">
        <property name="sequence">['source', 'detsys']</property>
        <facility name="source">sources/NeutronFromStorage</facility>
        <facility name="detsys">detectors/DetectorSystemFromXml</facility>

        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">1</property>

        <property name="ncount">10</property>

        <property name="multiple-scattering">False</property>

        <component name="source">
            <property name="path">scattered-neutrons</property>
        </component>

        <component name="detsys">
            <property name="tofparams">0,0.02,1e-7</property>
            <property name="instrumentxml">SEQUOIA.xml</property>
            <property name="eventsdat">events.dat</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="detsys">((0, 0, 0), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->

