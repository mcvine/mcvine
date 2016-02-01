FROM linjiao/mcvine-centos-deps:7

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

WORKDIR /opt/mcvine
RUN BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib64 ./build.py
