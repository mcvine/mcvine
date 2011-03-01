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
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!-- [SNS_source4] -> [PowderKernel] -> [DetectorSystem] -->

<!DOCTYPE inventory>

<inventory>

    <component name="ssd4">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/SNS_source4</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">detectorsystem</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">100000</property>
        <property name="buffer_size">10000</property>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">
            
            <property name="yh">0.085</property>
            <property name="dist">10</property>
            <property name="Emin">0.01</property>
            <property name="Emax">1000</property>
            <property name="tinmin">0.0</property>
            <property name="sample_t">1</property>
            <property name="height">0.12</property>
            <property name="width">0.10</property>
            <property name="proton_T">0.600</property>
            <property name="tinmax">2000.0</property>
            <property name="sample_E">2</property>
            <property name="S_filename">a1Gw2-8-f5_fit_fit.dat</property>
            <property name="xw">0.016</property>
            
        </component>

        <component name="sample">
            <property name="xml">Al_assembly2/sampleassembly.xml</property>
        </component>

        <component name="detector">
            <component name="m1">
                <property name="title">detector_l90tc</property>
                <property name="filename">tc.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="tmin">0</property>
                <property name="tmax">100</property>
                <property name="nt">100</property>
            </component>

            <component name="m2">
                <property name="title">detector_l90wc</property>
                <property name="filename">wc.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="wmin">0</property>
                <property name="wmax">10</property>
                <property name="nw">100</property>
            </component>
            
            <component name="m3">
                <property name="title">detector_l90tt</property>
                <property name="filename">tt.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="tmin">0</property>
                <property name="tmax">100</property>
                <property name="nt">100</property>
            </component>

            <component name="m4">
                <property name="title">detector_l90wt</property>
                <property name="filename">wt.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="wmin">0</property>
                <property name="wmax">10</property>
                <property name="nw">100</property>
            </component>

            <component name="m5">
                <property name="title">detector_l90tb</property>
                <property name="filename">tb.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="tmin">0</property>
                <property name="tmax">100</property>
                <property name="nt">100</property>
            </component>

            <component name="m6">
                <property name="title">detector_l90wb</property>
                <property name="filename">wb.txt</property>
                <property name="xwidth">0.770</property>
                <property name="yheight">0.385</property>
                <property name="wmin">0</property>
                <property name="wmax">10</property>
                <property name="nw">100</property>
            </component>

            <component name="geometer">
                <property name="m1">((-2, 0, 0), (0, 90, 0))</property>
                <property name="m2">((-2, 0, 0), (0, 90, 0))</property>
                <property name="m3">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="m4">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="m5">((-1.959, -0.403, 0), (0, 90, 0))</property>
                <property name="m6">((-1.959, -0.403, 0), (0, 90, 0))</property>
            </component>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 10), (0, 0, 0))</property>
            <property name="detector">((0, 0, 10), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>


