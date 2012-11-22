<inventory>

<component name="ssd">
<property name="sequence">['source', 'monitor_source_energy', 'monitor_source_tof', 'monitor_0', 'aperture_0', 'monitor_1', 'aperture_1', 'sample', 'detector', 'neutron_printer']</property>
<facility name="source">sources/Source_simple</facility>
<facility name="monitor_source_energy">monitors/E_monitor</facility>
<facility name="monitor_source_tof">monitors/TOF_monitor2</facility>
<facility name="monitor_0">monitors/NDMonitor(x,y,t)</facility>
<facility name="aperture_0">optics/Slit</facility>
<facility name="monitor_1">monitors/NDMonitor(x,y,t)</facility>
<facility name="aperture_1">optics/Slit</facility>
<facility name="sample">samples/SampleAssemblyFromXml</facility>
<facility name="detector">monitors/NDMonitor(x,y,t)</facility>
<facility name="neutron_printer">monitors/EventAreaMonitor</facility>

<property name="dump-instrument">False</property>
<property name="overwrite-datafiles">on</property>
<property name="launcher">mpirun</property>
<property name="output-dir">out</property>
<property name="ncount">1e6</property>
<property name="buffer_size">100000</property>
<property name="multiple-scattering">False</property>
<property name="mode">worker</property>
<facility name="geometer">geometer</facility>
<property name="dump-registry">False</property>

<component name="source">
<property name="yh">0.01</property>
<property name="dist">10.0</property>
<property name="width">0.0</property>
<property name="dE">2.0</property>
<property name="gauss">1</property>
<property name="height">0.0</property>
<property name="flux">1.0</property>
<property name="dLambda">0.0</property>
<property name="radius">0.05</property>
<property name="Lambda0">0.0</property>
<property name="E0">10.0</property>
<property name="xw">0.01</property>
</component>


<component name="monitor_source_energy">
<property name="nchan">20</property>
<property name="ymax">0.0</property>
<property name="Emin">0.0</property>
<property name="Emax">20.0</property>
<property name="yheight">0.2</property>
<property name="restore_neutron">False</property>
<property name="filename">monitor_source_energy.dat</property>
<property name="xmax">0.0</property>
<property name="xmin">0.0</property>
<property name="xwidth">0.2</property>
<property name="ymin">0.0</property>
<property name="name">e_monitor</property>
</component>

<component name="monitor_source_tof">
<property name="nchan">20</property>
<property name="tmin">0.002</property>
<property name="tmax">0.006</property>
<property name="restore_neutron">False</property>
<property name="filename">monitor_source_tof.dat</property>
<property name="xmax">0.2</property>
<property name="xmin">0.0</property>
<property name="ymax">0.2</property>
<property name="ymin">0.0</property>
</component>

<component name="monitor_0">
<property name="title">ixyt</property>
<property name="filename">monitor_0.h5</property>
<property name="tmin">0.00</property>
<property name="tmax">0.01</property>
<property name="nt">50</property>
<property name="nx">20</property>
<property name="ny">20</property>
<property name="xmin">-0.05</property>
<property name="ymin">-0.05</property>
<property name="xmax">0.05</property>
<property name="ymax">0.05</property>
</component>

<component name="aperture_0">
<property name="radius">0.1</property>
<property name="xmax">0.2</property>
<property name="xmin">0.0</property>
<property name="ymax">0.2</property>
<property name="ymin">0.0</property>
</component>

<component name="aperture_1">
<property name="radius">0.1</property>
<property name="xmax">0.2</property>
<property name="xmin">0.0</property>
<property name="ymax">0.2</property>
<property name="ymin">0.0</property>
</component>

<component name="monitor_1">
<property name="title">ixyt</property>
<property name="filename">monitor_1.h5</property>
<property name="tmin">0.00</property>
<property name="tmax">0.01</property>
<property name="nt">50</property>
<property name="nx">20</property>
<property name="ny">20</property>
<property name="xmin">-0.012</property>
<property name="ymin">-0.012</property>
<property name="xmax">0.012</property>
<property name="ymax">0.012</property>
</component>

<component name="sample">
<property name="xml">delta_QE/sampleassembly.xml</property>
</component>

<component name="detector">
<property name="title">ixyt</property>
<property name="filename">detector.h5</property>
<property name="tmin">0.00</property>
<property name="tmax">0.150</property>
<property name="nt">50</property>
<property name="nx">125</property>
<property name="ny">125</property>
<property name="xmin">-0.5</property>
<property name="ymin">-0.5</property>
<property name="xmax">0.5</property>
<property name="ymax">0.5</property>
<property name="xwidth">1</property>
<property name="yheight">1</property>

</component>


<component name="neutron_printer">
<property name="xmin">-0.5</property>
<property name="xmax">0.5</property>
<property name="nx">100</property>
<property name="ymin">-0.5</property>
<property name="ymax">0.5</property>
<property name="ny">100</property>
<property name="tofmin">0</property>
<property name="tofmax">0.02</property>
<property name="ntof">100</property>
</component>

<component name="geometer">
<property name="source">((0, 0, 0), (0, 0, 0))</property>
<property name="monitor_source_energy">((0, 0, 4.4), (0, 0, 0))</property>
<property name="monitor_source_tof">((0, 0, 4.4), (0, 0, 0))</property>
<property name="monitor_0">((0, 0, 4.5), (0, 0, 0))</property>
<property name="aperture_0">((0, 0, 7.0), (0, 0, 0))</property>
<property name="monitor_1">((0, 0, 10.5), (0, 0, 0))</property>
<property name="aperture_1">((0, 0, 10.7), (0, 0, 0))</property>
<property name="sample">((0, 0, 11.0), (0, 0, 0))</property>
<property name="detector">((0, 0, 16.0), (0, 0, 0))</property>
<property name="neutron_printer">((0, 0, 16.0), (0, 0, 0))</property>
</component>

</component>

</inventory>
