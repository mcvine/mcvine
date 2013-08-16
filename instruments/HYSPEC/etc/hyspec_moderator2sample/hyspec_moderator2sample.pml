<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                      (C) 2006-2013  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="hyspec_moderator2sample">
      
        <property name="sequence">[ 'moderator','mon0_tof','mon0_total','g1a_guide','g1b_guide', 'g1c_guide','t0_t1a_guide', 't1a_chopper','g2_curved_guide','g3_guide', 'shutter2_guide', 'shutter2_valve_guide','valve_mon1_guide', 'mon1_tof', 'mon1_total', 'mon1_t1b_guide','t1b_chopper', 't1b_t2_guide', 't2_fermi','t2_mon2_guide', 'mon2_tof', 'mon2_total','g4_guide','arm2','monochromator','exit_tube','mon3_tof', 'mon3_total','aperture1', 'soeller40', 'soeller20', 'aperture2','recorder']</property>

        <facility name="moderator">sources/SNS_source4</facility>
	<facility name="mon0_tof">monitors/TOF_monitor2</facility>
	<facility name="mon0_total">monitors/Monitor</facility>
        <facility name="g1a_guide">optics/Guide</facility>
        <facility name="g1b_guide">optics/Guide</facility>
        <facility name="g1c_guide">optics/Guide</facility>
        <facility name="t0_t1a_guide">optics/Guide</facility>
        <facility name="t1a_chopper">optics/Chopper_v_mark</facility>
        <facility name="g2_curved_guide">optics/Guide_curved_mark</facility>
        <facility name="g3_guide">optics/Guide</facility>
        <facility name="shutter2_guide">optics/Guide</facility>
        <facility name="shutter2_valve_guide">optics/Guide</facility>
        <facility name="valve_mon1_guide">optics/Guide</facility>
	<facility name="mon1_tof">monitors/TOF_monitor2</facility>
	<facility name="mon1_total">monitors/Monitor</facility>
        <facility name="mon1_t1b_guide">optics/Guide</facility>
        <facility name="t1b_chopper">optics/Chopper_v_mark</facility>
        <facility name="t1b_t2_guide">optics/Guide</facility>
        <facility name="t2_fermi">optics/FermiChopper_mark</facility>
        <facility name="t2_mon2_guide">optics/Guide</facility>
	<facility name="mon2_tof">monitors/TOF_monitor2</facility>
	<facility name="mon2_total">monitors/Monitor</facility>
        <facility name="monitor1">monitors/TOF_monitor2</facility>
        <facility name="g4_guide">optics/Guide</facility>
        <facility name="arm2">Dummy</facility>
        <facility name="monochromator">optics/Monochromator_curved</facility>
        <facility name="exit_tube">optics/Guide</facility>
	<facility name="mon3_tof">monitors/TOF_monitor2</facility>
	<facility name="mon3_total">monitors/Monitor</facility>
	<facility name="aperture1">optics/Slit</facility>
	<facility name="soeller40">optics/Collimator_linear</facility>
	<facility name="soeller20">optics/Collimator_linear</facility>
	<facility name="aperture2">optics/Slit</facility>
        <facility name="recorder">monitors/NeutronToStorage</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>

        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">False</property>

        <component name="moderator">
            <property name="S_filename">SNS_TD_30o70p_fit_fit.dat</property>
            <property name="width">0.1</property>
            <property name="height">0.12</property>
            <property name="dist">2.5</property>
            <property name="xw">0.04</property>
            <property name="yh">0.132</property>
            <property name="Emin">0.0</property>
            <property name="Emax">200.0</property>
            <property name="tinmin">0</property>
            <property name="tinmax">5000</property>
	    <property name="sample_E">2</property>
	    <property name="sample_t">1</property>
	    <property name="proton_T">0.7</property>
	    <property name="n_pulses">1</property>
	    <property name="delnfrac">1.e-30</property>
	    <property name="frequency">60</property>
	    <!-- Emin, Emax -->
        </component>

        <component name="mon0_tof">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
            <property name="nchan"> 1000.0 </property>
            <property name="filename"> mon0_tof.dat </property>
	    <!-- tmin, tmax -->
        </component>

        <component name="mon0_total">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
        </component>

        <component name="g1a_guide">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.132 </property>
            <property name="w2"> 0.04 </property>
            <property name="h2"> 0.141 </property>
            <property name="l"> 0 </property>
            <property name="R0"> 0.98 </property>
            <property name="m"> 3.0 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- l -->
        </component>

        <component name="g1b_guide">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.141 </property>
            <property name="w2"> 0.04 </property>
            <property name="h2"> 0.15 </property>
            <property name="l"> 0 </property>
            <property name="R0"> 0.98 </property>
            <property name="m"> 3.0 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- l -->
        </component>

        <component name="g1c_guide">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.15 </property>
            <property name="w2"> 0.04 </property>
            <property name="h2"> 0.15 </property>
            <property name="l"> 0 </property>
            <property name="R0"> 0.98 </property>
            <property name="m"> 3.0 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- l -->
        </component>

        <component name="t0_t1a_guide">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.15 </property>
            <property name="w2"> 0.04 </property>
            <property name="h2"> 0.15 </property>
            <property name="l"> 0 </property>
            <property name="R0"> 0.98 </property>
            <property name="m"> 3.0 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- l -->
        </component>

        <component name="t1a_chopper">
            <property name="n">1</property>
	    <!-- w, R, f, pha -->
        </component>

        <component name="g2_curved_guide">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.15 </property>
            <property name="l"> 0.500 </property>
            <property name="R0"> 0.98 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
            <property name="ml"> 3.0 </property>
            <property name="mb"> 3.0 </property>
            <property name="mt"> 3.0 </property>
            <property name="W"> 0.0001 </property>
            <property name="nseg"> 48 </property>
            <property name="dseg"> 0.001 </property>
            <property name="psi_out"> 0 </property>
            <property name="xout"> 0 </property>
            <property name="zout"> 0 </property>
	    <!-- mr,R -->
        </component>

        <component name="g3_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="shutter2_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="shutter2_valve_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="valve_mon1_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="mon1_tof">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
            <property name="filename"> mon1_tof.dat </property>
	    <!-- tmin, tmax, nchan -->
        </component>

        <component name="mon1_total">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
        </component>
	
        <component name="mon1_t1b_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="t1b_chopper">
            <property name="n">1</property>
	    <!-- w, R, f, pha -->
        </component>
	
        <component name="t1b_t2_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="t2_fermi">
            <property name="alpham">0</property>
            <property name="Qc">0</property>
            <property name="m">0</property>
            <property name="Wi">0.0001</property>
            <property name="R0">0</property>
	    <!-- dist, rad, nu, ymin, ymax, w, Nslit, Vi, slit, tran -->
        </component>

        <component name="t2_mon2_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="mon2_tof">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
            <property name="filename"> mon2_tof.dat </property>
	    <!-- tmin, tmax, nchan -->
        </component>

        <component name="mon2_total">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
        </component>

        <component name="g4_guide">
            <property name="R0"> 0.98 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
	    <!-- w1, h1, w2, h2, l, m -->
        </component>

        <component name="monochromator">
            <property name="r0">0.8</property>
            <property name="t0">0.0</property>
	    <!-- zwidth, yheight=wid_v, gap, NH, NV, mosaich, mosaicv, Q, RV, RH -->
        </component>

        <component name="exit_tube">
            <property name="w1"> 0.04 </property>
            <property name="h1"> 0.128 </property>
            <property name="w2"> 0.04 </property>
            <property name="h2"> 0.085 </property>
            <property name="l"> 0.3 </property>
            <property name="R0"> 0.98 </property>
            <property name="m"> 0 </property>
            <property name="W"> 0.0001 </property>
            <property name="Qc"> 0.022 </property>
            <property name="alpha">5.54</property>
        </component>


        <component name="mon3_tof">
            <property name="xmin"> -0.05 </property>
            <property name="xmax"> 0.05 </property>
            <property name="ymin"> -0.15 </property>
            <property name="ymax"> 0.15 </property>
            <property name="filename"> mon3_tof.dat </property>
	    <!-- tmin, tmax, nchan -->
        </component>

        <component name="mon3_total">
            <property name="xmin"> -0.03 </property>
            <property name="xmax"> 0.03 </property>
            <property name="ymin"> -0.10 </property>
            <property name="ymax"> 0.10 </property>
        </component>


        <component name="aperture1">
            <property name="width"> 0.02 </property>
            <property name="height"> 0.06 </property>
        </component>

        <component name="soeller40">
            <property name="xwidth"> 0.04 </property>
            <property name="yheight"> 0.08 </property>
            <property name="len"> 0.2 </property>
            <property name="divergence"> 40.0 </property>
        </component>

        <component name="soeller20">
            <property name="xwidth"> 0.04 </property>
            <property name="yheight"> 0.08 </property>
            <property name="len"> 0.2 </property>
            <property name="divergence"> 20.0 </property>
        </component>

        <component name="aperture2">
            <property name="width"> 0.017 </property>
            <property name="height"> 0.04 </property>
        </component>

	<component name="recorder">
            <property name="path">neutrons</property>
        </component>
	
	
        <component name="geometer">
            <property name="moderator">((0, 0, 0), (0, 0, 0))</property>
            <property name="mon0_tof">((0, 0, 2.3203-0.002), (0, 0, 0))</property>
            <property name="mon0_total">((0, 0, 2.3203-0.001), (0, 0, 0))</property>
            <property name="g1a_guide">((0, 0, 2.3203), (0, 0, 0))</property>
            <property name="g1b_guide">((0, 0, 4.2328), (0, 0, 0))</property>
            <property name="g1c_guide">((0, 0, 6.3203), (0, 0, 0))</property>
            <property name="t0_t1a_guide">((0, 0, 6.3203), (0, 0, 0))</property>
        </component>


    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Wed Jun  2 14:49:12 2010-->

<!-- End of file -->


