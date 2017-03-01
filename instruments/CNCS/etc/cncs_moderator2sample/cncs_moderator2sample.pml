<?xml version="1.0"?>
<inventory>
  <component name="cncs_moderator2sample">
    <property name="sequence">arm1,moderator,Guide1,FChopper,tof1b,Guide4,Chopper2,Guide5,Guide6,Guide7,Guide8,Chopper3,Guide9,Chopper41,Chopper42,tof3a,Guide10,Guide11,save_neutrons,Div_monh</property>
    <property name="arm1">Progress_bar</property>
    <property name="moderator">SNS_source</property>
    <property name="Guide1">Guide</property>
    <property name="FChopper">FermiChopper</property>
    <property name="tof1b">TOF_monitor</property>
    <property name="Guide4">Guide</property>
    <property name="Chopper2">DiskChopper_v2</property>
    <property name="Guide5">Guide</property>
    <property name="Guide6">Bender</property>
    <property name="Guide7">Guide</property>
    <property name="Guide8">Guide</property>
    <property name="Chopper3">DiskChopper_v2</property>
    <property name="Guide9">Guide</property>
    <property name="Chopper41">DiskChopper_v2</property>
    <property name="Chopper42">DiskChopper_v2</property>
    <property name="tof3a">TOF_monitor</property>
    <property name="Guide10">Guide</property>
    <property name="Guide11">Guide</property>
    <property name="save_neutrons">NeutronToStorage</property>
    <property name="Div_monh">DivPos_monitor</property>
    <component name="geometer">
      <property name="arm1">(0.0, 0.0, 0.0),(0, 0, 0)</property>
      <property name="moderator">relative((0.0, 0.0, 0.0), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Guide1">relative((0.0, 0.0, 1.002), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="FChopper">relative((0.0, 0.0, 6.413), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="tof1b">relative((0.0, 0.0, 6.555), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Guide4">relative((0.0, 0.0, 6.56), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Chopper2">relative((0.0, 0.0, 7.515), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Guide5">relative((0.0, 0.0, 7.572), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Guide6">relative((0.0, 0.0, 8.543), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
      <property name="Guide7">relative((0.0, 0.0, 23.544), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Guide8">relative((0.0, 0.0, 30.545), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Chopper3">relative((0.0, 0.0, 33.02), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Guide9">relative((0.0, 0.0, 33.025), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Chopper41">relative((0.0, 0.0, 34.784), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Chopper42">relative((0.0, 0.0, 34.785), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="tof3a">relative((0.0, 0.0, 34.836), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Guide10">relative((0.0, 0.0, 34.863), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Guide11">relative((0.0, 0.0, 35.762), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="save_neutrons">relative((0.0, 0.0, 36.114), to="arm1"),relative((0, 0, 0), to="arm1")</property>
      <property name="Div_monh">relative((0.0, 0.0, 36.264), to="arm1"),relative((0.0, 0.0, 0.0), to="arm1")</property>
    </component>
    
    <property name="multiple-scattering">off</property>
    <property name="ncount">1e6</property>
    <property name="buffer_size">100000</property>
    <property name="output-dir">out</property>
    <property name="overwrite-datafiles">off</property>
    
    <component name="arm1">
    </component>
    
    <component name="moderator">
      <property name="yh">0.14</property>
      <property name="xw">0.06</property>
      <property name="dist">1.0</property>
      <property name="Emin">4.0</property>
      <property name="Emax">6.0</property>
      <property name="S_filename">source_sct21a_td_05_1.dat</property>
      <property name="width">0.1</property>
      <property name="height">0.12</property>
    </component>
    
    <component name="Guide1">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.05</property>
      <property name="W">0.002</property>
      <property name="h2">0.1</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.1</property>
      <property name="m">2.5</property>
      <property name="l">5.28</property>
      <property name="w1">0.05</property>
    </component>
    
    <component name="FChopper">
      <property name="Nslit">9</property>
      <property name="zero_time">0</property>
      <property name="height">0.102</property>
      <property name="width">0.053</property>
      <property name="length">0.017</property>
      <property name="time">0.00660098767939</property>
      <property name="nu">60.0</property>
    </component>
    
    <component name="tof1b">
      <property name="ymin">-0.05</property>
      <property name="nchan">500</property>
      <property name="ymax">0.05</property>
      <property name="xmax">0.025</property>
      <property name="xmin">-0.025</property>
      <property name="t1">8000</property>
      <property name="t0">6000</property>
      <property name="filename">tof1b.det</property>
    </component>
    
    <component name="Guide4">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.05</property>
      <property name="W">0.002</property>
      <property name="h2">0.1</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.1</property>
      <property name="m">2.5</property>
      <property name="l">0.925</property>
      <property name="w1">0.05</property>
    </component>
    
    <component name="Chopper2">
      <property name="yheight">0</property>
      <property name="nslit">1</property>
      <property name="radius">0.25</property>
      <property name="theta_0">14.0</property>
      <property name="delay">0.007727743496</property>
      <property name="nu">60.</property>
    </component>
    
    <component name="Guide5">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.05</property>
      <property name="W">0.002</property>
      <property name="h2">0.1</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.1</property>
      <property name="m">2.5</property>
      <property name="l">0.965</property>
      <property name="w1">0.05</property>
    </component>
    
    <component name="Guide6">
      <property name="Qcs">0.02</property>
      <property name="alphas">5.0</property>
      <property name="R0s">0.99</property>
      <property name="ma">2.5</property>
      <property name="d">0.001</property>
      <property name="Wa">0.002</property>
      <property name="h">0.1</property>
      <property name="k">1</property>
      <property name="mi">3.5</property>
      <property name="l">14.98</property>
      <property name="Wi">0.002</property>
      <property name="R0a">0.99</property>
      <property name="Qca">0.02</property>
      <property name="r">2000.0</property>
      <property name="Ws">0.002</property>
      <property name="w">0.05</property>
      <property name="alphaa">5.0</property>
      <property name="R0i">0.99</property>
      <property name="Qci">0.02</property>
      <property name="alphai">5.0</property>
      <property name="ms">2.5</property>
    </component>
    
    <component name="Guide7">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.05</property>
      <property name="W">0.002</property>
      <property name="h2">0.1</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.1</property>
      <property name="m">3.0</property>
      <property name="l">7.0</property>
      <property name="w1">0.05</property>
    </component>
    
    <component name="Guide8">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.035</property>
      <property name="W">0.002</property>
      <property name="h2">0.0765</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.1</property>
      <property name="m">3.5</property>
      <property name="l">2.447</property>
      <property name="w1">0.05</property>
    </component>
    
    <component name="Chopper3">
      <property name="yheight">0</property>
      <property name="nslit">1</property>
      <property name="radius">0.25</property>
      <property name="theta_0">14.0</property>
      <property name="delay">0.0338056991247</property>
      <property name="nu">60</property>
    </component>
    
    <component name="Guide9">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.0218</property>
      <property name="W">0.002</property>
      <property name="h2">0.0597</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.076</property>
      <property name="m">3.5</property>
      <property name="l">1.7</property>
      <property name="w1">0.0332</property>
    </component>
    
    <component name="Chopper41">
      <property name="yheight">0.065</property>
      <property name="nslit">1</property>
      <property name="radius">0.2825</property>
      <property name="theta_0">9.0</property>
      <property name="delay">0.0356093264028</property>
      <property name="nu">-300</property>
    </component>
    
    <component name="Chopper42">
      <property name="yheight">0.065</property>
      <property name="nslit">1</property>
      <property name="radius">0.2825</property>
      <property name="theta_0">9.0</property>
      <property name="delay">0.0356093264028</property>
      <property name="nu">300</property>
    </component>
    
    <component name="tof3a">
      <property name="ymin">-0.05</property>
      <property name="nchan">60</property>
      <property name="ymax">0.05</property>
      <property name="xmax">0.025</property>
      <property name="xmin">-0.025</property>
      <property name="t1">35768.5713939</property>
      <property name="t0">35468.5713939</property>
      <property name="filename">tof3a.det</property>
    </component>
    
    <component name="Guide10">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.0152</property>
      <property name="W">0.002</property>
      <property name="h2">0.0503</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.0587</property>
      <property name="m">3.5</property>
      <property name="l">0.875</property>
      <property name="w1">0.0211</property>
    </component>
    
    <component name="Guide11">
      <property name="Qc">0.02</property>
      <property name="R0">0.99</property>
      <property name="w2">0.015</property>
      <property name="W">0.002</property>
      <property name="h2">0.05</property>
      <property name="alpha">5.0</property>
      <property name="h1">0.05</property>
      <property name="m">4.0</property>
      <property name="l">0.22</property>
      <property name="w1">0.015</property>
    </component>
    
    <component name="save_neutrons">
      <property name="path">neutrons</property>
    </component>
    
    <component name="Div_monh">
      <property name="maxdiv">5</property>
      <property name="yheight">0.1</property>
      <property name="filename">Divh_Sample.dat</property>
      <property name="npos">500</property>
      <property name="xwidth">0.1</property>
      <property name="ndiv">500</property>
    </component>
    
  </component>
</inventory>
