<?xml version="1.0"?>
<!DOCTYPE inventory>

<inventory>

    <component name="sqekernel-test">
        <property name="ncount">10000.0</property>
        <property name="output-dir">out.sqekernel-test</property>
        <property name="overwrite-datafiles">False</property>
        <property name="sequence">['source', 'sample', 'monitor']</property>
        <facility name="source">sources/MonochromaticSource</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="monitor">monitors/IQE_monitor</facility>

        <component name="source">
            <property name="probability">1.0</property>
            <property name="energy">100.</property>
            <property name="velocity">[0.0, 0.0, 1.0]</property>
            <property name="height">0.0</property>
            <property name="width">0.0</property>
            <property name="energy-width">0.0</property>
            <property name="time">0.0</property>
            <property name="position">[0.0, 0.0, 0.0]</property>
        </component>

        <component name="sample">
            <property name="xml">sampleassemblies/Ni-sqekernel/sampleassembly.xml</property>
        </component>

        <component name="monitor">
            <property name="Ei">100.0</property>
            <property name="Qmin">0.0</property>
            <property name="Qmax">13.0</property>
            <property name="nQ">130</property>
            <property name="Emin">-75.0</property>
            <property name="Emax">75.0</property>
            <property name="nE">150</property>
            <property name="min_angle_in_plane">0.0</property>
            <property name="max_angle_in_plane">120.0</property>
            <property name="min_angle_out_of_plane">-30.0</property>
            <property name="max_angle_out_of_plane">30.0</property>
            <property name="filename">iqe_monitor.dat</property>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 1), (0, 0, 0))</property>
            <property name="monitor">((0, 0, 1), (0, 0, 0))</property>
        </component>

    </component>

</inventory>

<!-- End of file -->


