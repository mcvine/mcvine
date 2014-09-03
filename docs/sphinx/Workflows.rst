.. _workflows:

Workflows
=========

.. note::
   Under construction.


The basic procedure of using a workflow template is:

* copy the template (a directory of the workflow control file,
  scripts and input files) to a working directory
* make changes to the sample assembly (a directory)
* run the workflow

The main task for the MCViNE workflow user is ususally simplified 
to setting up the sample assembly.
A sample assembly in MCViNE is specified by a directory of xml files
and associated data files.
One xml file named ``sampleassembly.xml'' always exists and it is the
leading specification file. 
For each scatterer in the sample assembly, there is one xml file named
as ``<name>-scatterer.xml''.

The following is a simplified sampleassembly.xml for
a sample assembly consisting of one single
vanadium plate

.. (the full example can be found at XXX dropbox??? XXX
.. \href{https://www.dropbox.com/sh/089o37vkv22ip11/AADfRcVSyk\_ZXjI9cfMUn8-Sa}{MCViNE
..  examples at dropbox},
.. and click ``sampleassemblies'' and then ``vanadium-plate''):

::

   <SampleAssembly name="bcc V powder sample assembly" >
   
   <PowderSample name="V" type="sample">
     <Shape>
       <block width="50*mm" height="50*mm" thickness="1.2*mm" />
     </Shape>
   </PowderSample>
   
   <LocalGeometer>
     <Register name="V" position="(0,0,0)" orientation="(0,0,45)"/>
   </LocalGeometer>
   
   </SampleAssembly>

The vanadium plate is specified as a powder sample named ``V'' 
with a ``block'' of given dimensions, oriented at 45 degree away from the
default position perpendicular to the beam. 

Since the vanadium plate scatterer is named ``V'' in sampleassembly.xml, 
MCViNE expects a ``V-scatterer.xml'' to describe
scattering properties of that scatterer::

 <homogeneous_scatterer max_multiplescattering_loops="4" >
  
  <KernelContainer average="yes">
    
    <Phonon_IncoherentElastic_Kernel dw_core='0.007014*angstrom**2'/>
    
    <Phonon_IncoherentInelastic_Kernel>
      <LinearlyInterpolatedDOS idf-data-path="V-phonons/DOS"/>
    </Phonon_IncoherentInelastic_Kernel>
    
    <MultiPhonon_Kernel Qmax="20/angstrom">
      <LinearlyInterpolatedDOS idf-data-path="V-phonons/DOS"/>
    </MultiPhonon_Kernel>
    
  </KernelContainer>

 </homogeneous_scatterer>


The user specifies the scattering function of the V scatterer 
by choosing scattering kernels to be put into V-scatterer.xml, 
and setting parameters for the chosen kernels.


