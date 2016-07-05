# conda recipe for building mcvine

This is different from what is in
http://github.com/mcvine/conda-recipes,
which contains 
(danse-ins-conda-cmake-drivers)[https://github.com/danse-inelastic/conda-packaging]
to build conda pkgs
of mcvine deps and mantid and mcvine.
The cmake-driver allows setting things like version 
number and git branch from the master
CMakeLists.txt at the src root dir.

This one does not need the cmake driver,
but it does use cmake for the building step
as the other recipe.

## Configuration

* Modify meta.yaml
  - version
  - git_rev
  - git_url
