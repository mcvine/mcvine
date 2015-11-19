In conversion from mm/config to cmake, we have relied on 
experiences gained in converting danse/ins packages.
mcvine is more complex since it has several sub-packages.

The pull request: #15

The sequence of conversion:
* mcni
* mccomposite
* mccomponents
* mcvine
* mcstas2
* instruments/ARCS

The tests were kind of new.
Added tools into cmake_utils for discovering and adding 
python tests and c++ tests.

In newer cmake (such as 3.2.2), target name cannot have "/".

ENVIRONMENT variables are tricky at times.
Sometimes they can be added (set_tests_properties)

Installation of binaries was done by installing a directory.
Need to set permissions in install command.

Auto-generation of mcstas2 components is tricky.
* Added a rule to generate the source codes for the components
* Then a rule to rerun cmake configuration step
* And then we can call make again to make all the bindings
  for these components

