<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                             Jiao Lin, Alex Dementsov
!                      California Institute of Technology
!                      (C) 2006-2010  All Rights Reserved
!
! {LicenseText}
!
! Testing PowderN with NDMonitor
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!-- [Source_simple] -> [PowderN] -> [NDMonitor] -->

<!DOCTYPE inventory>

<inventory>

    <component name="ssd5_1">
        <property name="sequence">['source', 'sample', 'detector']</property>
        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/PowderN</facility>
        <facility name="detector">monitors/NDMonitor(x,y,t)</facility>
        
        <property name="dump-instrument">False</property>
        <property name="overwrite-datafiles">on</property>
        <property name="launcher">mpirun</property>
        <property name="output-dir">out</property>
        <property name="ncount">500000</property>
        <property name="multiple-scattering">False</property>
        <property name="mode">worker</property>
        <facility name="geometer">geometer</facility>
        <property name="buffer_size">0</property>
        <property name="dump-registry">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="source">
            <property name="yh">0.01</property>
            <property name="dist">10.0</property>
            <property name="width">0.0</property>
            <property name="dE">70.0</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.05</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">100.0</property>
            <property name="xw">0.01</property>
        </component>


        <component name="sample">

            <property name="reflections">Al.laz</property>
            <property name="yheight">0.1</property>
            <property name="xwidth">0.1</property>
            <property name="zthick">0.01</property>
            <property name="DW">0</property>
            <property name="Delta_d">1e-5</property>
            <property name="frac">0</property>
            <property name="tfrac">0</property>

        </component>


        <component name="detector">
            <property name="title">ixyt</property>
            <property name="filename">ixyt.h5</property>
            <property name="tmin">0.0</property>
            <property name="tmax">0.002</property>
            <property name="nt">100</property>
            <property name="nx">200</property>
            <property name="ny">200</property>
            <property name="xmax">1.0</property>
            <property name="xmin">-1.0</property>
            <property name="ymin">-1.0</property>
            <property name="ymax">1.0</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 10), (0, 0, 0))</property>
            <property name="detector">((0, 0, 11), (0, 0, 0))</property>
        </component>


    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Mon Feb 14 11:56:43 2011-->

<!-- End of file -->
<!--
 automatically created by the following command:
 $ ssd -source=Source_simple -sample=SampleAssemblyFromXml -detector=NDMonitor(x,y,t) -h -dump-pml=yes
-->
