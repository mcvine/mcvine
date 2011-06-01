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
        <property name="sequence">['source', 'detector']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="detector">detectors/DetectorSystemFromXml</facility>
	
        <property name="multiple-scattering">False</property>
	
        <property name="ncount">10.0</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>
	

        <component name="source">
            <property name="velocity">0,0,1</property>
        </component>


        <component name="detector">
            <property name="tofparams">0,0.02,1e-7</property>
            <property name="instrumentxml">ARCS.xml</property>
            <property name="eventsdat">events.dat</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 13.6), (0, 0, 0))</property>
            <property name="detector">((0, 0, 13.6), (0, 0, 0))</property>
        </component>


    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->

