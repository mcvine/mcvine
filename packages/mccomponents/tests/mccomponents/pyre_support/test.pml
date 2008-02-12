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

    <component name="test">
        <property name="typos">strict</property>
        <property name="help-persistence">False</property>
        <property name="help">False</property>
        <property name="output-dir">out</property>
        <property name="sequence">['source', 'sample', 'detector']</property>
        <property name="ncount">10000.0</property>
        <facility name="sample">sample</facility>
        <facility name="source">source</facility>
        <property name="help-properties">False</property>
        <property name="help-components">False</property>
        <property name="overwrite-datafiles">False</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">1000</property>
        <facility name="detector">detector</facility>

        <component name="sample">
            <property name="xml">Ni.xml</property>
            <property name="help-properties">False</property>
            <property name="help-persistence">False</property>
            <property name="help">False</property>
            <property name="help-components">False</property>
        </component>


        <component name="source">
            <property name="help-persistence">False</property>
            <property name="help">False</property>
            <property name="probability">1.0</property>
            <property name="help-properties">False</property>
            <property name="velocity">0,0,3000</property>
            <property name="help-components">False</property>
            <property name="time">0.0</property>
            <property name="position">0,0,0</property>
        </component>


        <component name="weaver">
            <property name="help-persistence">False</property>
            <property name="help">False</property>
            <property name="copyright">2007</property>
            <property name="creator"></property>
            <property name="timestamp">True</property>
            <property name="author">Jiao Lin</property>
            <property name="bannerCharacter">~</property>
            <property name="help-properties">False</property>
            <property name="versionId"> $Id$</property>
            <property name="timestampLine"> Generated automatically by %s on %s</property>
            <property name="help-components">False</property>
            <property name="lastLine"> End of file </property>
            <property name="licenseText">['{LicenseText}']</property>
            <property name="copyrightLine">(C) %s  All Rights Reserved</property>
            <property name="organization">California Institute of Technology</property>
            <property name="bannerWidth">78</property>
        </component>


        <component name="detector">
            <property name="help-persistence">False</property>
            <property name="help">False</property>
            <property name="eventsdat">events.dat</property>
            <property name="tofparams">0,3e-3,1e-5</property>
            <property name="help-properties">False</property>
            <property name="instrumentxml">ARCS.xml</property>
            <property name="help-components">False</property>
        </component>


        <component name="geometer">
            <property name="help-persistence">False</property>
            <property name="help">False</property>
            <property name="sample">((0, 0, 10), (0, 0, 0))</property>
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="help-properties">False</property>
            <property name="help-components">False</property>
            <property name="detector">((0, 0, 10), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Tue Feb 12 10:57:55 2008-->

<!-- End of file -->
