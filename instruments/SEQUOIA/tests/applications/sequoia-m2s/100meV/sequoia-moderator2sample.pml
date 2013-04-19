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

    <component name="sequoia-moderator2sample">
        <facility name="t_mon2">monitors/TOF_monitor2</facility>
        <property name="dump-instrument">False</property>
        <facility name="geometer">geometer</facility>
        <property name="output-dir">out</property>
        <facility name="adjustable_slits">optics/Slit</facility>
        <facility name="shutter_guide">obsolete/Channeled_guide</facility>
        <facility name="mod">sources/SNS_source</facility>
        <facility name="guide13">obsolete/Channeled_guide</facility>
        <property name="sequence">[u'arm1', u'mod', u'core_ves', u'shutter_guide', u'guide1', u'guide2', u'guide3', u'guide4', u'guide5', u'guide6', u'guide7', u'guide8', u'guide9', u'guide10', u'guide11', u't0_chopp', u'guide13', u'guide14', u'guide15', u'guide16', u'guide17', u'guide18', u'guide19', u'guide20', u'guide21', u'guide22', u'guide23', u'guide24', u'guide25', u'guide26', u'guide27', u'fermi_chopp', u'adjustable_slits', u'Monitor1', u'guide29', u'guide31', u'guide32', u'guide34', u'E_det', u'recorder', u't_mon2']</property>
        <property name="ncount">10000.0</property>
        <facility name="guide29">obsolete/Channeled_guide</facility>
        <facility name="guide21">obsolete/Channeled_guide</facility>
        <facility name="guide20">obsolete/Channeled_guide</facility>
        <facility name="E_det">monitors/E_monitor</facility>
        <facility name="guide22">obsolete/Channeled_guide</facility>
        <facility name="guide25">obsolete/Channeled_guide</facility>
        <facility name="guide24">obsolete/Channeled_guide</facility>
        <facility name="guide27">obsolete/Channeled_guide</facility>
        <facility name="guide26">obsolete/Channeled_guide</facility>
        <facility name="recorder">monitors/NeutronToStorage</facility>
        <property name="multiple-scattering">False</property>
        <property name="fermi_chopp">fermichopper-1</property>
        <facility name="t0_chopp">optics/Vertical_T0</facility>
        <facility name="guide8">obsolete/Channeled_guide</facility>
        <facility name="guide9">obsolete/Channeled_guide</facility>
        <facility name="guide6">obsolete/Channeled_guide</facility>
        <facility name="guide7">obsolete/Channeled_guide</facility>
        <facility name="guide4">obsolete/Channeled_guide</facility>
        <facility name="guide5">obsolete/Channeled_guide</facility>
        <facility name="guide2">obsolete/Channeled_guide</facility>
        <facility name="guide3">obsolete/Channeled_guide</facility>
        <facility name="core_ves">obsolete/Channeled_guide</facility>
        <facility name="guide1">obsolete/Channeled_guide</facility>
        <facility name="guide34">obsolete/Channeled_guide</facility>
        <property name="dump-registry">False</property>
        <facility name="guide32">obsolete/Channeled_guide</facility>
        <facility name="guide31">obsolete/Channeled_guide</facility>
        <property name="launcher">mpirun</property>
        <facility name="Monitor1">monitors/TOF_monitor2</facility>
        <facility name="arm1">optics/Arm</facility>
        <facility name="guide11">obsolete/Channeled_guide</facility>
        <facility name="guide18">obsolete/Channeled_guide</facility>
        <facility name="guide19">obsolete/Channeled_guide</facility>
        <property name="overwrite-datafiles">False</property>
        <facility name="guide14">obsolete/Channeled_guide</facility>
        <facility name="guide15">obsolete/Channeled_guide</facility>
        <facility name="guide16">obsolete/Channeled_guide</facility>
        <facility name="guide17">obsolete/Channeled_guide</facility>
        <facility name="guide10">obsolete/Channeled_guide</facility>
        <property name="tracer">no-neutron-tracer</property>
        <facility name="guide23">obsolete/Channeled_guide</facility>

        <component name="t_mon2">
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


        <component name="fermichopper-1">
            <property name="nchan">16.0</property>
            <property name="ymax">0.0325</property>
            <property name="max_iter">0</property>
            <property name="len">0.1</property>
            <property name="nu">600.0</property>
            <property name="bw">0.0005</property>
            <property name="w">0.06</property>
            <property name="delta">0.0</property>
            <property name="ymin">-0.0325</property>
            <property name="tc">0.00411573267923</property>
            <property name="blader">1.53</property>
            <property name="name">fermi_chop2</property>
        </component>


        <component name="guide17">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08004</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07881</property>
            <property name="w2">0.06782</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06872</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide8">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08988</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.08908</property>
            <property name="w2">0.07538</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07597</property>
            <property name="d">0.0</property>
        </component>


        <component name="adjustable_slits">
            <property name="cut">0.0</property>
            <property name="ymax">0.04</property>
            <property name="height">0.0</property>
            <property name="width">0.0</property>
            <property name="radius">0.0</property>
            <property name="xmax">0.04</property>
            <property name="xmin">-0.04</property>
            <property name="ymin">-0.04</property>
            <property name="name">slit</property>
        </component>


        <component name="shutter_guide">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.0999</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">1.83743</property>
            <property name="h2">0.09456</property>
            <property name="w2">0.0794</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">2.5</property>
            <property name="mx">2.5</property>
            <property name="w1">0.08294</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide29">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.06166</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.228</property>
            <property name="h2">0.0607</property>
            <property name="w2">0.05473</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0554</property>
            <property name="d">0.0</property>
        </component>


        <component name="E_det">
            <property name="nchan">200</property>
            <property name="ymax">0.025</property>
            <property name="Emin">80.0</property>
            <property name="Emax">120.0</property>
            <property name="yheight">0.2</property>
            <property name="restore_neutron">False</property>
            <property name="filename">IE.dat</property>
            <property name="xmax">0.025</property>
            <property name="xmin">-0.025</property>
            <property name="xwidth">0.2</property>
            <property name="ymin">-0.025</property>
            <property name="name">e_monitor</property>
        </component>


        <component name="guide21">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.0748</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07335</property>
            <property name="w2">0.06382</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06488</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide20">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07619</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.0748</property>
            <property name="w2">0.06488</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0659</property>
            <property name="d">0.0</property>
        </component>


        <component name="recorder">
            <property name="path">neutrons</property>
        </component>


        <component name="guide1">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09456</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09398</property>
            <property name="w2">0.07898</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.0794</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide25">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.06858</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.06684</property>
            <property name="w2">0.05911</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06036</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide24">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07024</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.06858</property>
            <property name="w2">0.06036</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06156</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide27">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.06502</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.0631</property>
            <property name="w2">0.05643</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0578</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide26">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.06684</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.06502</property>
            <property name="w2">0.0578</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05911</property>
            <property name="d">0.0</property>
        </component>


        <component name="mpirun">
            <property name="dry">False</property>
            <property name="nodelist">[]</property>
            <property name="extra"></property>
            <property name="python-mpi">`which python`</property>
            <property name="command">mpirun</property>
            <property name="debug">False</property>
            <property name="nodes">0</property>
        </component>


        <component name="t0_chopp">
            <property name="ymax">0.045</property>
            <property name="len">0.474</property>
            <property name="nu">60.0</property>
            <property name="w2">0.101</property>
            <property name="w1">0.08</property>
            <property name="delta">0.0</property>
            <property name="ymin">-0.045</property>
            <property name="tc">0.00228671523681</property>
            <property name="name">vertical_t0</property>
        </component>


        <component name="geometer">
            <property name="t_mon2">(relative((0.0, 0.0, 29.0032), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="dump">False</property>
            <property name="adjustable_slits">(relative((0.0, 0.0, 18.25), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="shutter_guide">(relative((0.0, 0.0, 2.2988), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="transformer">coordinate-system-transformer</property>
            <property name="guide3">(relative((0.0, 0.0, 5.164), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide29">(relative((0.0, 0.0, 18.2604), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide21">(relative((0.0, 0.0, 14.436), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide20">(relative((0.0, 0.0, 13.944), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide23">(relative((0.0, 0.0, 15.42), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="mod">(relative((0.0, 0.0, 0.0), to='arm1'), relative((0, 0, 0), to='arm1'))</property>
            <property name="guide25">(relative((0.0, 0.0, 16.404), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide24">(relative((0.0, 0.0, 15.912), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide27">(relative((0.0, 0.0, 17.388), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide26">(relative((0.0, 0.0, 16.896), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="recorder">(relative((0.0, 0.0, 19.9), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="fermi_chopp">(relative((0.0, 0.0, 18.0), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="t0_chopp">(relative((0.0, 0.0, 10.0), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide8">(relative((0.0, 0.0, 7.574), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide9">(relative((0.0, 0.0, 8.056), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide6">(relative((0.0, 0.0, 6.61), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide7">(relative((0.0, 0.0, 7.092), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide4">(relative((0.0, 0.0, 5.646), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide5">(relative((0.0, 0.0, 6.128), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide2">(relative((0.0, 0.0, 4.682), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="E_det">(relative((0.0, 0.0, 1.99), to='fermi_chopp'), relative((0, 0, 0), to='fermi_chopp'))</property>
            <property name="core_ves">(relative((0.0, 0.0, 1.0106), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide1">(relative((0.0, 0.0, 4.2), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide34">(relative((0.0, 0.0, 19.4164), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide22">(relative((0.0, 0.0, 14.928), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide32">(relative((0.0, 0.0, 18.9569), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide31">(relative((0.0, 0.0, 18.4984), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="Monitor1">(relative((0.0, 0.0, 18.26), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="arm1">((0.0, 0.0, 0.0), (0, 0, 0))</property>
            <property name="guide18">(relative((0.0, 0.0, 12.96), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide19">(relative((0.0, 0.0, 13.452), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide14">(relative((0.0, 0.0, 10.992), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide15">(relative((0.0, 0.0, 11.484), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide16">(relative((0.0, 0.0, 11.976), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide17">(relative((0.0, 0.0, 12.468), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide10">(relative((0.0, 0.0, 8.538), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide11">(relative((0.0, 0.0, 9.02), to='mod'), relative((0, 0, 0), to='mod'))</property>
            <property name="guide13">(relative((0.0, 0.0, 10.5), to='mod'), relative((0, 0, 0), to='mod'))</property>
        </component>


        <component name="guide9">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08908</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.08825</property>
            <property name="w2">0.07477</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07538</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide6">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09137</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09064</property>
            <property name="w2">0.07653</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07707</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide7">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09064</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.08988</property>
            <property name="w2">0.07597</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07653</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide4">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09274</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09207</property>
            <property name="w2">0.07758</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07807</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide5">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09207</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09137</property>
            <property name="w2">0.07707</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07758</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide2">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09398</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09337</property>
            <property name="w2">0.07854</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07898</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide3">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.09337</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.09274</property>
            <property name="w2">0.07807</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.0</property>
            <property name="mx">3.0</property>
            <property name="w1">0.07854</property>
            <property name="d">0.0</property>
        </component>


        <component name="core_ves">
            <property name="alphay">5.5</property>
            <property name="R0">0.0</property>
            <property name="name">channeled_guide</property>
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


        <component name="mod">
            <property name="yh">0.12</property>
            <property name="dist">0.995</property>
            <property name="name">sns_source</property>
            <property name="Emin">80.0</property>
            <property name="Emax">120.0</property>
            <property name="S_filename">source_sct521_bu_17_1.dat</property>
            <property name="width">0.0923</property>
            <property name="height">0.1113</property>
            <property name="xw">0.1</property>
        </component>


        <component name="guide23">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07183</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07024</property>
            <property name="w2">0.06156</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06271</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide34">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.05654</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.409</property>
            <property name="h2">0.05456</property>
            <property name="w2">0.05043</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05181</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide22">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07335</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07183</property>
            <property name="w2">0.06271</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06382</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide32">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.05866</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.4585</property>
            <property name="h2">0.05655</property>
            <property name="w2">0.05181</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.05328</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide31">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.06066</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.4585</property>
            <property name="h2">0.05866</property>
            <property name="w2">0.05328</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.0547</property>
            <property name="d">0.0</property>
        </component>


        <component name="arm1">
            <property name="name">arm</property>
        </component>


        <component name="guide18">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07881</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07753</property>
            <property name="w2">0.06688</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06782</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide19">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.07753</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.07619</property>
            <property name="w2">0.0659</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06688</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide14">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08344</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.08235</property>
            <property name="w2">0.07042</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07123</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide15">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08235</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.08122</property>
            <property name="w2">0.06959</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07042</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide16">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08122</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.08004</property>
            <property name="w2">0.06872</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.06959</property>
            <property name="d">0.0</property>
        </component>


        <component name="Monitor1">
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


        <component name="guide10">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08825</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.08738</property>
            <property name="w2">0.07413</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07477</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide11">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08738</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.482</property>
            <property name="h2">0.08648</property>
            <property name="w2">0.07346</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07413</property>
            <property name="d">0.0</property>
        </component>


        <component name="guide13">
            <property name="alphay">5.5</property>
            <property name="R0">0.98</property>
            <property name="name">channeled_guide</property>
            <property name="h1">0.08449</property>
            <property name="alphax">5.5</property>
            <property name="Qcy">0.02</property>
            <property name="Qcx">0.02</property>
            <property name="l">0.492</property>
            <property name="h2">0.08344</property>
            <property name="w2">0.07123</property>
            <property name="W">0.002</property>
            <property name="k">1.0</property>
            <property name="my">3.6</property>
            <property name="mx">3.6</property>
            <property name="w1">0.07199</property>
            <property name="d">0.0</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Fri Apr 19 08:59:00 2013-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ sequoia-m2s -h -dump-pml -E_det.Emin=80.0 -adjustable_slits.xmin=-0.04 -E_det.Emax=120.0 -fermi_chopp=fermichopper-1 -mod.Emax=120.0 -mod.Emin=80.0 -fermi_chopp.nu=600.0 -t0_chopp.nu=60.0 -adjustable_slits.ymin=-0.04 -t0_chopp.tc=0.00228671523681 -adjustable_slits.xmax=0.04 -adjustable_slits.ymax=0.04 -fermi_chopp.tc=0.00411573267923
-->

