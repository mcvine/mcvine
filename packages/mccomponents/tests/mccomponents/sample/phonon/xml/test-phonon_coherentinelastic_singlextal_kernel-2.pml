<?xml version="1.0"?>

<!DOCTYPE inventory>

<inventory>

  <component name="test-phonon_coherentinelastic_singlextal_kernel-2">

    <facility name="source">sources/MonochromaticSource</facility>
    <facility name="sample">samples/SampleAssemblyFromXml</facility>
    <facility name="detector">monitors/IQE_monitor</facility>

    <property name="overwrite-datafiles">yes</property>
    <property name="ncount">10000</property>
    <property name="buffer_size">10000</property>
    <property name="output-dir">out-phonon_coherentinelastic_singlextal_kernel-2</property>

    <component name="source">
      <property name="position">[0.0, 0.0, 0.0]</property>
      <property name="energy">10</property>
      <property name="velocity">[0.0, 0.0, 1.0]</property>
      <property name="probability">1.0</property>
      <property name="time">0.0</property>
    </component>

    <component name="sample">
      <property name="xml">sampleassemblies/coh-inel-singlextal/sampleassembly.xml</property>
    </component>

    <component name="detector">
      <property name="max_angle_out_of_plane">90</property>
      <property name="min_angle_out_of_plane">-90</property>
      <property name="max_angle_in_plane">180</property>
      <property name="min_angle_in_plane">-180</property>
      <property name="filename">IQE.dat</property>
      <property name="Ei">10.0</property>
      <property name="Emax">9.9</property>
      <property name="Emin">-10.0</property>
      <property name="nE">100</property>
      <property name="Qmin">0.0</property>
      <property name="Qmax">4.5</property>
      <property name="nQ">90</property>
      <property name="min_angle_out_of_plane">-30.0</property>
      <property name="max_angle_out_of_plane">30.0</property>
      <property name="filename">iqe_monitor.dat</property>
    </component>

    <component name="geometer">
      <property name="source">((0, 0, 0), (0, 0, 0))</property>
      <property name="sample">((0, 0, 10), (0, 0, 0))</property>
      <property name="detector">((0, 0, 10), (0, 0, 0))</property>
    </component>


    <component name="journal">
      <component name="debug">
	<property name="CoherentInelastic_SingleXtal">on</property>
	<property name="Omega_minus_deltaE ctor">on</property>
	<property name="Omega_minus_deltaE">on</property>
      </component>
    </component>

  </component>

</inventory>


<!-- End of file -->
