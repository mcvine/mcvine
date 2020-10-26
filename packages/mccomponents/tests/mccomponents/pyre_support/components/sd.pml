<?xml version="1.0"?>
<!DOCTYPE inventory>

<inventory>

    <component name="sd">
        <property name="sequence">['source', 'detector']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="detector">detectors/DetectorSystemFromXml</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000</property>

        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">1</property>


        <component name="source">
            <property name="energy">0.0</property>
            <property name="position">[0.0, 0.0, 0.0]</property>
            <property name="velocity">[1500, 0.0, 2000]</property>
            <property name="probability">1.0</property>
            <property name="time">0.0</property>
        </component>


        <component name="detector">
            <property name="tofparams">0,10e-3,1e-4</property>
            <property name="instrumentxml">ARCS.xml</property>
            <property name="eventsdat">events.dat</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="detector">((0, 0, 0), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- End of file -->

