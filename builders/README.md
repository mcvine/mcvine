# Various things about building mcvine

Sub dirs:

* dev: setup dev environment
* travis-conda: conda recipe used by travis build. see ../travis.yml
* notes: misc notes
* runtests
* test-release
* docker: used to create distributions. no longer in active development after we migrate to conda
* recipes: recipes to build mcvine on NERSC and FERMI. will phase out soon because conda CentOS6 build of mcvine seems to be working fine at least for FERMI