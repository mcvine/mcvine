.. _tutorials-powder-kernel:

Tutorials -- Powder Kernel
==========================

Simulation with Powder Kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this tutorial we will do experiment with a simple instrument consisting of three
components:

::

[Source_simple] -> [PowderKernel] -> [NDMonitor(x,y,t)]

that uses **SimplePowderDiffractionKernel**, or simply **Powder Kernel**. The structure
of configration and execution files for the instrument looks like the following:

::

    ssd         # execution Python script
    ssd.pml     # main configuration file
    Al/
        Al-scatterer.xml
        Al.laz
        Al.xyz
        peaks.py
        sampleassembly.xml

The main configuration file ssd.pml defines components, order of components in
the instrument and parameters for each component. Let's take a look at the ssd.pml file

**ssd.pml**

::

    <?xml version="1.0"?>
    
    <!-- [Source_simple] -> [PowderKernel] -> [NDMonitor(x,y,t)] -->

    <!DOCTYPE inventory>

    <inventory>

        <component name="ssd">
            <property name="sequence">['source', 'sample', 'detector']</property>
            <facility name="source">sources/Source_simple</facility>
            <facility name="sample">samples/SampleAssemblyFromXml</facility>
            <facility name="detector">monitors/NDMonitor(x,y,t)</facility>

            <property name="dump-instrument">False</property>
            <property name="overwrite-datafiles">on</property>
            <property name="launcher">mpirun</property>
            <property name="output-dir">out</property>
            <property name="ncount">100000</property>
            <property name="buffer_size">10000</property>
            <property name="multiple-scattering">False</property>
            <property name="mode">worker</property>
            <facility name="geometer">geometer</facility>
            <property name="dump-registry">False</property>

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
                <property name="xml">Al/sampleassembly.xml</property>
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

::

 Note: Base name of the file ssd.pml should be the same as in tag
       <component name="ssd"> otherwise simulation will silently
       die without doing anything useful.

::

 Note: Name "ssd" stands for initial letters of source -> sample -> detector

The ssd.pml file has three components: Source_simple, SampleAssemblyFromXml and
NDMonitor(x,y,t). It describes parameters for source and detector components
whereas parameters for sample component are defined in a separate file:
"Al/sampleassembly.xml". Let's take a closer look at the components.

Source_simple
-------------

Source_simple component is a standard component available in McStas simulation package.
It generates flux of neutrons uniformly distributed in the energy range ``[E0-dE, E0+dE]`` in meV.
In our configuration the energy range is ``[30, 170] meV``. Parameters ``xw``, ``yh`` and
``dist`` define width, height and distance to the sample correspondingly. The benefit
of using this simple source is to quickly get an estimate of what happens to the neutrons
in this energy range as they propagates through the instrument.


SampleAssemblyFromXml
---------------------

The purpose
of the kernel is to describe a general mechanism of neutron scattering without 
regard to any macroscopic properties of the material. It does though depend on
microscopic properties such as atom species, lattice parameters, symmetry of the
lattice, scattering cross sections etc.



Al/sampleassembly.xml::

    <?xml version="1.0"?>

    <!DOCTYPE SampleAssembly>

    <SampleAssembly name="Al">

      <PowderSample name="Al" type="sample">
        <Shape>
          <block width="6*cm" height="10*cm" thickness="1*cm" />
        </Shape>
        <Phase type="crystal">
          <ChemicalFormula>Al</ChemicalFormula>
          <xyzfile>Al.xyz</xyzfile>
        </Phase>
      </PowderSample>

      <LocalGeometer registry-coordinate-system="InstrumentScientist">
        <Register name="Al" position="(0,0,0)" orientation="(0,0,0)"/>
      </LocalGeometer>

    </SampleAssembly>

Al/Al.xyz::

    4
    4.049320 0 0   0 4.049320 0   0 0 4.049320
    Al 0  0  0
    Al 0.5 0.5 0
    Al 0.5 0 0.5
    Al 0 0.5 0.5

Al/Al-scatterer.xml::

    <?xml version="1.0"?>

    <!DOCTYPE scatterer>

    <!-- weights: absorption, scattering, transmission -->
    <homogeneous_scatterer mcweights="0, 1, 0">

      <SimplePowderDiffractionKernel Dd_over_d="1e-5" DebyeWaller_factor="1" peaks-py-path="peaks.py">
      </SimplePowderDiffractionKernel>

    </homogeneous_scatterer>

peaks.py::

    from mccomponents.sample.diffraction.SimplePowderDiffractionKernel import Peak

    peaks = [
        Peak(q=2.687561, F_squared=1.690000, multiplicity=8, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=3.103329, F_squared=1.690000, multiplicity=6, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=4.388769, F_squared=1.440000, multiplicity=12, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=5.146288, F_squared=1.440000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=5.375123, F_squared=1.210000, multiplicity=8, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=6.206657, F_squared=1.210000, multiplicity=6, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=6.763548, F_squared=1.000000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=6.939254, F_squared=1.000000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=7.601572, F_squared=1.000000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=8.062684, F_squared=0.810000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=8.062684, F_squared=0.810000, multiplicity=8, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=8.777539, F_squared=0.640000, multiplicity=12, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=9.179770, F_squared=0.640000, multiplicity=48, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=9.309986, F_squared=0.640000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=9.309986, F_squared=0.640000, multiplicity=6, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=9.813587, F_squared=0.490000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=10.174943, F_squared=0.490000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=10.292577, F_squared=0.490000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=10.750246, F_squared=0.490000, multiplicity=8, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.081100, F_squared=0.360000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.081100, F_squared=0.360000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.189210, F_squared=0.360000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.611592, F_squared=0.360000, multiplicity=48, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.918560, F_squared=0.360000, multiplicity=24, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=11.918560, F_squared=0.360000, multiplicity=48, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
        Peak(q=12.413314, F_squared=0.250000, multiplicity=6, intrinsic_line_width=0.000000, DebyeWaller_factor=0.000000),
    ]



Al/Al.laz::

    # TITLE *Aluminum-Al-[FM3-M] Miller, H.P.jr.;DuMond, J.W.M.[1942] at 298 K
    # CELL 4.049320 4.049320 4.049320 90.000000 90.000000 90.000000
    # SPCGRP F M 3 M   CUBIC STRUCTURE
    # ATOM AL 1 0.000000 0.000000 0.000000
    # SCATTERING FACTOR  COEFFICIENTS: AL     F= 0.345 CM-12
    # Reference: Physical Review (1940) 57, 198-206
    #
    # Physical parameters:
    # sigma_coh 1.495   coherent scattering cross section in [barn]
    # sigma_inc 0.0082  incoherent scattering cross section in [barn]
    # sigma_abs 0.231   absorption scattering cross section in [barn]
    # density   2.70    in [g/cm^3]
    # weight    26.98   in [g/mol]
    # nb_atoms  4       in [atoms/unit cell]
    # v_sound   5100    in [m/s]
    # v_sound_l 6420    velocity of longitudinal sound in [m/s]
    # v_sound_t 3040    velocity of transversal sound in [m/s]
    # T_m       933.5   melting temperature in [K]
    # T_b       2792.2  boiling temperature in [K]
    # At_number 13      atomic number Z
    # lattice_a 4.04932 lattice parameter a in [Angs]
    #
    # Format parameters: Lazy format <http://icsd.ill.fr>
    # column_j 17 multiplicity 'j'
    # column_d 6  d-spacing 'd' in [Angs]
    # column_F 13 norm of scattering factor |F| in [barn^0.5]
    # column_h 1
    # column_k 2
    # column_l 3
    #
    # H  K  L  THETA  2THETA D VALUE  1/D**2 SIN2*1000  H  K  L INTENSITY         /F(HKL)/       A(HKL)      B(HKL) PHA.ANG. MULT   LPG
      1  1  1  12.35  24.70   2.3379  0.1830    45.74   1  1  1    1000.0              1.3         1.32         0.00    0.00  8  22.38
      2  0  0  14.30  28.59   2.0247  0.2439    60.99   2  0  0     550.0              1.3         1.30         0.00    0.00  6  16.92
      2  2  0  20.44  40.88   1.4317  0.4879   121.97   2  2  0     503.5              1.2         1.22         0.00    0.00 12   8.75
      3  1  1  24.18  48.35   1.2209  0.6709   167.71   3  1  1     686.4              1.2         1.17         0.00    0.00 24   6.54
      2  2  2  25.32  50.65   1.1689  0.7318   182.96   2  2  2     205.3              1.1         1.15         0.00    0.00  8   6.05
      4  0  0  29.60  59.20   1.0123  0.9758   243.95   4  0  0     106.3              1.1         1.08         0.00    0.00  6   4.71
      3  3  1  32.56  65.13   0.9290  1.1587   289.69   3  3  1     337.1              1.0         1.03         0.00    0.00 24   4.10
      4  2  0  33.52  67.04   0.9055  1.2197   304.93   4  2  0     314.0              1.0         1.02         0.00    0.00 24   3.93
      4  2  2  37.22  74.45   0.8266  1.4637   365.92   4  2  2     242.5              1.0         0.96         0.00    0.00 24   3.43
      5  1  1  39.91  79.82   0.7793  1.6466   411.66   5  1  1     204.2              0.9         0.91         0.00    0.00 24   3.17
      3  3  3  39.91  79.82   0.7793  1.6466   411.66   3  3  3      68.1              0.9         0.91         0.00    0.00  8   3.17
      4  4  0  44.31  88.61   0.7158  1.9516   487.89   4  4  0      79.3              0.8         0.85         0.00    0.00 12   2.86
      5  3  1  46.93  93.86   0.6845  2.1345   533.63   5  3  1     277.3              0.8         0.81         0.00    0.00 48   2.74
      4  4  2  47.81  95.61   0.6749  2.1955   548.88   4  4  2     132.9              0.8         0.80         0.00    0.00 24   2.71
      6  0  0  47.81  95.61   0.6749  2.1955   548.88   6  0  0      33.2              0.8         0.80         0.00    0.00  6   2.71
      6  2  0  51.35 102.69   0.6403  2.4395   609.87   6  2  0     113.9              0.7         0.75         0.00    0.00 24   2.63
      5  3  3  54.07 108.13   0.6175  2.6224   655.61   5  3  3     102.9              0.7         0.72         0.00    0.00 24   2.60
      6  2  2  54.99 109.98   0.6105  2.6834   670.85   6  2  2      99.8              0.7         0.71         0.00    0.00 24   2.60
      4  4  4  58.81 117.63   0.5845  2.9274   731.84   4  4  4      29.9              0.7         0.66         0.00    0.00  8   2.64
      5  5  1  61.86 123.72   0.5670  3.1103   777.58   5  5  1      84.6              0.6         0.63         0.00    0.00 24   2.73
      7  1  1  61.86 123.72   0.5670  3.1103   777.58   7  1  1      84.6              0.6         0.63         0.00    0.00 24   2.73
      6  4  0  62.92 125.85   0.5615  3.1713   792.83   6  4  0      83.4              0.6         0.62         0.00    0.00 24   2.77
      6  4  2  67.52 135.04   0.5411  3.4153   853.82   6  4  2     163.1              0.6         0.59         0.00    0.00 48   3.06
      5  5  3  71.52 143.05   0.5272  3.5982   899.56   5  5  3      85.2              0.6         0.56         0.00    0.00 24   3.51
      7  3  1  71.52 143.05   0.5272  3.5982   899.56   7  3  1     170.5              0.6         0.56         0.00    0.00 48   3.51
      8  0  0  81.05 162.10   0.5062  3.9032   975.79   8  0  0      34.4              0.5         0.52         0.00    0.00  6   6.59


NDMonitor(x,y,t)
----------------


ssd::

    #!/usr/bin/env python

    import mcvine
    import mccomponents.sample.diffraction.xml

    def main():
        from mcvine.applications.InstrumentBuilder import build
        components = ['source', 'sample', 'detector']
        App = build(components)
        app = App('ssd')
        app.run()
        return

    if __name__ == '__main__':
        main()


::

 $ python ssd

Draw plot use script

plot_ndmonitor.py::

    #!/usr/bin/env python

    # Note: Before using this script make sure that "out/ixyt.h5" is generated!
    from histogram.hdf import load
    from histogram.plotter import defaultPlotter as dp

    h   = load('out/ixyt.h5', 'ix_y_t')
    ixy = h.sum('t')

    dp.plot(ixy)


.. figure:: images/powder-kernel.png
   :width: 450px

   *Fig. 1 Diffraction image from PowderKernel simulation*


Simulation with PowderN
^^^^^^^^^^^^^^^^^^^^^^^

ssd2.pml::

    <?xml version="1.0"?>

    <!-- [Source_simple] -> [PowderN] -> [NDMonitor(x,y,t)] -->

    <!DOCTYPE inventory>

    <inventory>

        <component name="ssd">
            <property name="sequence">['source', 'sample', 'detector']</property>
            <facility name="source">sources/Source_simple</facility>
            <facility name="sample">samples/SampleAssemblyFromXml</facility>
            <facility name="detector">monitors/NDMonitor(x,y,t)</facility>

            <property name="dump-instrument">False</property>
            <property name="overwrite-datafiles">on</property>
            <property name="launcher">mpirun</property>
            <property name="output-dir">out</property>
            <property name="ncount">100000</property>
            <property name="buffer_size">10000</property>
            <property name="multiple-scattering">False</property>
            <property name="mode">worker</property>
            <facility name="geometer">geometer</facility>
            <property name="dump-registry">False</property>

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
            <property name="xwidth">0.06</property>
            <property name="yheight">0.1</property>
            <property name="zthick">0.01</property>
            <property name="DW">1</property>
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


ssd2::

    #!/usr/bin/env python

    import mcvine
    import mccomponents.sample.diffraction.xml

    def main():
        from mcvine.applications.InstrumentBuilder import build
        components = ['source', 'sample', 'detector']
        App = build(components)
        app = App('ssd2')
        app.run()
        return

    if __name__ == '__main__':
        main()

::

 $ python ssd2



.. figure:: images/powderN.png
   :width: 450px

   *Fig. 2 Diffraction image with PowderN component*
