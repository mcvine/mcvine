FROM linjiao/mcvine-fedora-deps:21

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

# prepare 
RUN mkdir -p /opt
WORKDIR /opt
RUN git clone https://github.com/mcvine/releaser.git mcvine

# build
WORKDIR /opt/mcvine
RUN BOOSTPYTHON_DIR=/usr BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib64 ./build.py
