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

    <component name="arcs_analyze_beam">
        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/NeutronFromStorage</facility>
        <facility name="monitor">beam_analyzer</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">1e6</property>
        <property name="buffer_size">100000</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>

        <property name="dump-instrument">False</property>
        <property name="dump-registry">False</property>

        <component name="source">
            <property name="path">neutrons</property>
        </component>


	<component name="monitor">

            <component name="mtof">
                <property name="tofmin">0</property>
                <property name="tofmax">0.016</property>
                <property name="ntof">100</property>
            </component>

            <component name="menergy">
                <property name="energymin">0</property>
                <property name="energymax">100</property>
                <property name="nenergy">100</property>
            </component>

            <component name="mx_y">
                <property name="xmin">-0.05</property>
                <property name="xmax">0.05</property>
                <property name="nx">100</property>
                <property name="ymin">-0.05</property>
                <property name="ymax">0.05</property>
                <property name="ny">100</property>
            </component>

            <component name="mx_divx">
                <property name="xmin">-0.05</property>
                <property name="xmax">0.05</property>
                <property name="nx">100</property>
                <property name="divxmin">-0.01</property>
                <property name="divxmax">0.01</property>
                <property name="ndivx">100</property>
            </component>

            <component name="mx_divy">
                <property name="xmin">-0.05</property>
                <property name="xmax">0.05</property>
                <property name="nx">100</property>
                <property name="divymin">-0.01</property>
                <property name="divymax">0.01</property>
                <property name="ndivy">100</property>
            </component>

            <component name="my_divx">
                <property name="ymin">-0.05</property>
                <property name="ymax">0.05</property>
                <property name="ny">100</property>
                <property name="divxmin">-0.01</property>
                <property name="divxmax">0.01</property>
                <property name="ndivx">100</property>
            </component>

            <component name="my_divy">
                <property name="ymin">-0.05</property>
                <property name="ymax">0.05</property>
                <property name="ny">100</property>
                <property name="divymin">-0.01</property>
                <property name="divymax">0.01</property>
                <property name="ndivy">100</property>
            </component>

        </component>


        <component name="geometer">
            <property name="source">((0, 0, 13.45), (0, 0, 0))</property>
            <property name="monitor">((0, 0, 13.6), (0, 0, 0))</property>
        </component>

	
    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Thu Jan  6 09:36:22 2011-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ arcs_analyze_beam -source=NeutronFromStorage -monitor=beam_analyzer -dump-pml=yes -h
-->

