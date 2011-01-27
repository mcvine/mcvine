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

<!DOCTYPE inventory>

<inventory>

    <component name="ssd4">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/SNS_source4</facility>
        <!--<facility name="source">sources/Source_simple</facility>-->
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">detectorsystem</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">100000</property>
        <property name="buffer_size">10000</property>

        <property name="overwrite-datafiles">True</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">
            <!--
            <property name="yh">0.1</property>
            <property name="dist">10.0</property>
            <property name="name">source_simple</property>
            <property name="width">0.0</property>
            <property name="dE">10.0</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.05</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">60.0</property>
            <property name="xw">0.1</property>
            -->
            
            <property name="yh">0.085</property>
            <property name="dist">4.3</property>
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
            <property name="xml">Al_SimplePowderDiffractionKernel/sampleassembly.xml</property>
        </component>

        <component name="detector">
            <component name="m1">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">100</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">tc.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">time</property>
            </component>

            <component name="m2">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">10</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">wc.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">wavelength</property>
            </component>
            
            <component name="m3">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">100</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">tt.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">time</property>
            </component>

            <component name="m4">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">10</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">wt.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">wavelength</property>
            </component>

            <component name="m5">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">100</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">tb.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">time</property>
            </component>

            <component name="m6">
                <property name="nxchan">1</property>
                <property name="format">table</property>
                <property name="bmax">10</property>
                <property name="yheight">0.385</property>
                <property name="restore_neutron">1</property>
                <property name="filename">wb.txt</property>
                <property name="nychan">1</property>
                <property name="bmin">0</property>
                <property name="deltab">0</property>
                <property name="nbchan">100</property>
                <property name="xwidth">0.770</property>
                <property name="type">wavelength</property>
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
            <property name="sample">((0, 0, 2), (0, 0, 0))</property>
            <property name="detector">((0, 0, 2), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>


