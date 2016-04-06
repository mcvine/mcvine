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

    <component name="arcs_moderator2sample">
        <property name="dump-instrument">False</property>
        <property name="fermichopper">fermichopper-100-1.5-SMI</property>
        <property name="output-dir">out</property>
        <facility name="guide511">optics/Dummy</facility>
        <facility name="shutter_guide">optics/Guide_channeled</facility>
        <facility name="guide123">optics/Guide_channeled</facility>
        <facility name="guide122">optics/Guide_channeled</facility>
        <facility name="guide121">optics/Guide_channeled</facility>
        <facility name="guide412">optics/Guide_channeled</facility>
        <facility name="guide411">optics/Guide_channeled</facility>
        <facility name="guide311">optics/Guide_channeled</facility>
        <facility name="t0chopper">optics/Vertical_T0</facility>
        <facility name="monitor">monitors/NeutronToStorage</facility>
        <property name="sequence">['moderator', 'core_vessel_insert', 'shutter_guide', 'guide111', 'guide112', 'guide113', 'guide121', 'guide122', 'guide123', 'guide131', 'guide132', 'guide133', 't0chopper', 'guide211', 'guide212', 'guide213', 'guide214', 'guide215', 'fermichopper', 'monitor1', 'guide311', 'guide411', 'guide412', 'guide511', 'monitor', 'monitor2']</property>
        <facility name="core_vessel_insert">optics/Guide_channeled</facility>
        <property name="ncount">10000.0</property>
        <property name="dump-registry">False</property>
        <facility name="guide215">optics/Guide_channeled</facility>
        <facility name="guide214">optics/Guide_channeled</facility>
        <facility name="guide211">optics/Guide_channeled</facility>
        <facility name="guide213">optics/Guide_channeled</facility>
        <facility name="guide212">optics/Guide_channeled</facility>
        <property name="multiple-scattering">False</property>
        <facility name="guide131">optics/Guide_channeled</facility>
        <facility name="guide132">optics/Guide_channeled</facility>
        <facility name="guide133">optics/Guide_channeled</facility>
        <facility name="guide112">optics/Guide_channeled</facility>
        <facility name="guide113">optics/Guide_channeled</facility>
        <facility name="geometer">geometer</facility>
        <facility name="guide111">optics/Guide_channeled</facility>
        <facility name="monitor2">monitors/TOF_monitor2</facility>
        <facility name="monitor1">monitors/TOF_monitor2</facility>
        <facility name="moderator">sources/SNS_source_r1</facility>
        <property name="launcher">mpirun</property>
        <property name="overwrite-datafiles">False</property>
        <property name="tracer">no-neutron-tracer</property>

        <component name="mpirun">
            <property name="dry">False</property>
            <property name="nodelist">[]</property>
            <property name="extra"></property>
            <property name="python-mpi">`which python`</property>
            <property name="command">mpirun</property>
            <property name="debug">False</property>
            <property name="nodes">0</property>
        </component>


        <component name="shutter_guide">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.09404</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">1.853</property>
            <property name="h2">0.08688</property>
            <property name="w2">0.07088</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">2.5</property>
            <property name="mx">2.5</property>
            <property name="w1">0.07493</property>
            <property name="d">0.0</property>
        </component>


        <component name="moderator">
            <property name="yh">0.12</property>
            <property name="dist">2.5</property>
            <property name="name">sns_source_r1</property>
            <property name="Emin">80.0</property>
            <property name="Emax">120.0</property>
            <property name="S_filename">source_sct521_bu_17_1.dat</property>
            <property name="width">0.1</property>
            <property name="height">0.12</property>
            <property name="xw">0.1</property>
        </component>


        <component name="guide122">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.08197</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.0806</property>
            <property name="w2">0.0671</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06792</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide121">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.08329</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.08197</property>
            <property name="w2">0.06792</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06871</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide412">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.05674</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.46275</property>
            <property name="h2">0.05408</property>
            <property name="w2">0.05187</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05331</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide411">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.05924</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.46275</property>
            <property name="h2">0.05674</property>
            <property name="w2">0.05331</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05468</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide311">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.06046</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.225</property>
            <property name="h2">0.05931</property>
            <property name="w2">0.05473</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05536</property>
            <property name="d">0.0</property>
        </component>


        <component name="t0chopper">
            <property name="ymax">0.045</property>
            <property name="len">0.474</property>
            <property name="nu">60.0</property>
            <property name="w2">0.101</property>
            <property name="w1">0.08</property>
            <property name="delta">0.0</property>
            <property name="ymin">-0.045</property>
            <property name="tc">0.00200550380504</property>
            <property name="name">vertical_t0</property>
        </component>


        <component name="monitor">
            <property name="path">neutrons</property>
        </component>


        <component name="guide215">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.06417</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.40204</property>
            <property name="h2">0.06227</property>
            <property name="w2">0.05637</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05745</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide214">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.06598</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.40204</property>
            <property name="h2">0.06417</property>
            <property name="w2">0.05745</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05848</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide211">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.07094</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.40204</property>
            <property name="h2">0.06936</property>
            <property name="w2">0.06044</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06136</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide213">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.06771</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.40204</property>
            <property name="h2">0.06598</property>
            <property name="w2">0.05848</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05948</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide212">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.06936</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.40204</property>
            <property name="h2">0.06771</property>
            <property name="w2">0.05948</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06044</property>
            <property name="d">0.0</property>
        </component>


        <component name="core_vessel_insert">
            <property name="alphay">5.5</property>
            <property name="R0">0.0</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.11323</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">1.2444</property>
            <property name="h2">0.102362</property>
            <property name="w2">0.084684</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.094285</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide131">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.07917</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.07766</property>
            <property name="w2">0.06534</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06624</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide132">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.07766</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.07609</property>
            <property name="w2">0.0644</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06534</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide133">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.07609</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.07443</property>
            <property name="w2">0.06342</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0644</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide112">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.08573</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.08454</property>
            <property name="w2">0.06947</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07019</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide113">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.08454</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.08329</property>
            <property name="w2">0.06871</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06947</property>
            <property name="d">0.0</property>
        </component>


        <component name="geometer">
            <property name="guide411">((0, 0, 12.08825), (0, 0, 0))</property>
            <property name="dump">False</property>
            <property name="guide511">((0, 0, 13.0183), (0, 0, 0))</property>
            <property name="shutter_guide">((0, 0, 2.2679), (0, 0, 0))</property>
            <property name="guide123">((0, 0, 6.59049), (0, 0, 0))</property>
            <property name="guide122">((0, 0, 6.1069), (0, 0, 0))</property>
            <property name="guide121">((0, 0, 5.62331), (0, 0, 0))</property>
            <property name="guide412">((0, 0, 12.55105), (0, 0, 0))</property>
            <property name="fermichopper">((0, 0, 11.61), (0, 0, 0))</property>
            <property name="guide311">((0, 0, 11.84975), (0, 0, 0))</property>
            <property name="t0chopper">((0, 0, 8.77), (0, 0, 0))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="monitor">((0, 0, 13.45), (0, 0, 0))</property>
            <property name="guide215">((0, 0, 11.0834), (0, 0, 0))</property>
            <property name="guide214">((0, 0, 10.68131), (0, 0, 0))</property>
            <property name="guide211">((0, 0, 9.47504), (0, 0, 0))</property>
            <property name="guide213">((0, 0, 10.27922), (0, 0, 0))</property>
            <property name="guide212">((0, 0, 9.87713), (0, 0, 0))</property>
            <property name="core_vessel_insert">((0, 0, 1.0106), (0, 0, 0))</property>
            <property name="guide131">((0, 0, 7.07433), (0, 0, 0))</property>
            <property name="guide132">((0, 0, 7.55792), (0, 0, 0))</property>
            <property name="guide133">((0, 0, 8.04145), (0, 0, 0))</property>
            <property name="guide112">((0, 0, 4.65589), (0, 0, 0))</property>
            <property name="guide113">((0, 0, 5.13948), (0, 0, 0))</property>
            <property name="guide111">((0, 0, 4.1723), (0, 0, 0))</property>
            <property name="monitor2">((0, 0, 18.5), (0, 0, 0))</property>
            <property name="monitor1">((0, 0, 11.831), (0, 0, 0))</property>
            <property name="moderator">((0, 0, 0), (0, 0, 0))</property>
        </component>


        <component name="guide111">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.08688</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.08573</property>
            <property name="w2">0.07019</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07088</property>
            <property name="d">0.0</property>
        </component>


        <component name="monitor2">
            <property name="nchan">20000</property>
            <property name="tmin">0.0</property>
            <property name="ymax">0.035</property>
            <property name="tmax">0.02</property>
            <property name="restore_neutron">False</property>
            <property name="filename">mon2-tof.dat</property>
            <property name="xmax">0.035</property>
            <property name="xmin">-0.035</property>
            <property name="ymin">-0.035</property>
            <property name="name">tof_monitor2</property>
        </component>


        <component name="monitor1">
            <property name="nchan">20000</property>
            <property name="tmin">0.0</property>
            <property name="ymax">0.035</property>
            <property name="tmax">0.02</property>
            <property name="restore_neutron">False</property>
            <property name="filename">mon1-tof.dat</property>
            <property name="xmax">0.035</property>
            <property name="xmin">-0.035</property>
            <property name="ymin">-0.035</property>
            <property name="name">tof_monitor2</property>
        </component>


        <component name="guide123">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">guide_channeled</property>
            <property name="h1">0.0806</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.48354</property>
            <property name="h2">0.07917</property>
            <property name="w2">0.06624</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0671</property>
            <property name="d">0.0</property>
        </component>


        <component name="fermichopper-100-1.5-SMI">
            <property name="nchan">31.0</property>
            <property name="ymax">0.0325</property>
            <property name="max_iter">10000</property>
            <property name="len">0.1</property>
            <property name="nu">600.0</property>
            <property name="bw">0.00041</property>
            <property name="w">0.060364</property>
            <property name="delta">0.0</property>
            <property name="ymin">-0.0325</property>
            <property name="tc">0.0026548049971</property>
            <property name="blader">0.5801</property>
            <property name="name">fermi_chop2</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Wed Apr  6 07:00:11 2016-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ M2S.pyc -dump-pml=yes -h -fermichopper.tc=0.0026548049971 -t0chopper.nu=60.0 -fermichopper.nu=600.0 -moderator.Emin=80.0 -fermichopper=fermichopper-100-1.5-SMI -t0chopper.tc=0.00200550380504 -moderator.Emax=120.0
-->

