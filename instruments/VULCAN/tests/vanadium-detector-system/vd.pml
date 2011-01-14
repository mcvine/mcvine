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

    <component name="vulcan-ssd">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/SNS_source4</facility>
        <facility name="sample">samples/V_sample</facility>
        <facility name="detector">detectorsystem</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">
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
            <property name="target_index">0</property>
            <property name="radius_i">0.015</property>
            <property name="radius_o">0.02</property>
            <property name="focus_aw">0</property>
            <property name="focus_yh">1.30</property>
            <property name="V0">13.827</property>
            <property name="zthick">0</property>
            <property name="focus_ah">0</property>
            <property name="sig_i">4.935</property>
            <property name="f_QE">0</property>
            <property name="frac">1</property>
            <property name="sig_a">5.08</property>
            <property name="target_z">0</property>
            <property name="target_x">-2</property>
            <property name="target_y">0</property>
            <property name="focus_r">0</property>
            <property name="h">0.05</property>
            <property name="yheight">0</property>
            <property name="focus_xw">0.780</property>
            <property name="xwidth">0</property>
            <property name="gamma">0</property>
            <property name="pack">1</property>
            <property name=""></property>
        </component>




        



        <component name="detector">
            <component name="tc">
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

            <component name="wc">
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
            
            <component name="tt">
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

            <component name="wt">
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

            <component name="tb">
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

            <component name="wb">
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
                <property name="tc">((-2, 0, 0), (0, 90, 0))</property>
                <property name="wc">((-2, 0, 0), (0, 90, 0))</property>
                <property name="tt">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="wt">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="tb">((-1.959, -0.403, 0), (0, 90, 0))</property>
                <property name="wb">((-1.959, -0.403, 0), (0, 90, 0))</property>
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


