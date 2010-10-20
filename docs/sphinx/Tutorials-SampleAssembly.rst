.. _tutorials-sampleassembly:

Sample Assembly
===============

Basics:

 * The main file is a xml file that descibes the composition of the sample assembly
 * Each neutron scatterer in the assembly has one xml file describing its scattering properties (scattering kernels)
 * Materials are defined using xyz files
 * Additional files may be needed for complex kernels 

Isotropic Elastic scattering Vanadium sample
--------------------------------------------
Create a directory:

  $ mkdir V
  $ cd V

So we are now inside directory V.
We need to create three files in this directory:

1. sampleassembly.xml -- the main file describes the whole sample assembly. It only contains one scatterer, V powder sample, in this case
2. V.xyz -- xyz file describing the crystal structure of V, the material
3. V-scatterer.xml  -- The file describing the kernels of the scatterer, the V sample.

Here are the contents of these files:

sampleassembly.xml::

 <SampleAssembly name="bcc V powder sample assembly">
  
  <PowderSample name="V" type="sample">
    <Shape>
      <block width="100*mm" height="100*mm" thickness="2*mm" />
    </Shape>
    <Phase type="crystal">
      <ChemicalFormula>V</ChemicalFormula>
      <xyzfile>V.xyz</xyzfile>
    </Phase>
  </PowderSample>
  
  <LocalGeometer registry-coordinate-system="InstrumentScientist">
    <Register name="V" position="(0,0,0)" orientation="(0,0,45)"/>
  </LocalGeometer>
 
 </SampleAssembly>


V.xyz::

 2
 3.02 0 0   0 3.02 0   0 0 3.02
 V 0  0  0
 V 0.5 0.5 0.5

V-scatterer.xml::

 <?xml version="1.0"?>
 
 <!DOCTYPE scatterer>
 
 <!-- mcweights: monte-carlo weights for 3 possible processes: 
 absorption, scattering, transmission -->
 <homogeneous_scatterer mcweights="0, 1, 0">
  
  <IsotropicKernel>
  </IsotropicKernel>
 
 </homogeneous_scatterer>


Single Crystal Phonon Coherent Inelastic Scattering fcc Ni
----------------------------------------------------------
Create a directory

  $ mkdir Ni
  $ cd Ni

So we are now inside directory $workdir/scattering/V.
We need to create three files in this directory:

1. sampleassembly.xml -- the main file describes the whole sample assembly. It only contains one scatterer, fcc Ni powder sample, in this case
2. Ni.xyz -- xyz file describing the crystal structure of Ni, the material
3. Ni-scatterer.xml  -- The file describing the kernels of the scatterer, the Ni sample.
4. a directory of idf files containing data of phonons on a reciprocal space grid.

Here are the contents of these files:

sampleassembly.xml::

 <SampleAssembly name="fcc Ni powder sample assembly">
  
  <PowderSample name="Ni" type="sample">
    <Shape>
      <block width="100*mm" height="100*mm" thickness="2*mm" />
    </Shape>
    <Phase type="crystal">
      <ChemicalFormula>Ni</ChemicalFormula>
      <xyzfile>Ni.xyz</xyzfile>
    </Phase>
  </PowderSample>
  
  <LocalGeometer registry-coordinate-system="InstrumentScientist">
    <Register name="Ni" position="(0,0,0)" orientation="(0,0,45)"/>
  </LocalGeometer>
 
 </SampleAssembly>


Ni.xyz::

 4
 3.52 0 0   0 3.52 0   0 0 3.52
 Ni 0  0  0
 Ni 0.5 0.5 0
 Ni 0.5 0 0.5
 Ni 0 0.5 0.5

Ni-scatterer.xml::

 <?xml version="1.0"?>
 
 <!DOCTYPE scatterer>
 
 <!-- mcweights: monte-carlo weights for 3 possible processes: 
 absorption, scattering, transmission -->
 <homogeneous_scatterer mcweights="0, 1, 0">
  
  <Phonon_CoherentInelastic_SingleXtal_Kernel>
    <LinearlyInterpolatedDispersion idf-data-path="phonon-dispersion"/>
  </Phonon_CoherentInelastic_SingleXtal_Kernel>
 
 </homogeneous_scatterer>

Directory "phonon-dispersion". All files in this directory
comply with the "idf" data format defined in 
http://danse.us/trac/inelastic/browser/idf.

 * DOS: phonon density of states
 * Omega2: square of angular freqencies of phonons on a grid
 * Polarizations: polarization vectors of phonons on a grid
 * Qgridinfo: definition of the reciprocal space grid

Please be very careful on providing these files to make sure
the units are correct in the data files.

