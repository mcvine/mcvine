FROM linjiao/mcvine-ubuntu-deps:14.04

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

# prepare 
RUN mkdir -p /opt/danse/src/mcvine
WORKDIR /opt/danse/src/mcvine
RUN git clone https://github.com/mcvine/releaser

# build
WORKDIR /opt/danse/src/mcvine/releaser
RUN . /opt/danse/bin/setup-danse.sh && BOOSTPYTHON_DIR=/usr BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib/x86_64-linux-gnu ./build.py
