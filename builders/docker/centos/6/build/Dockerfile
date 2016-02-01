FROM linjiao/mcvine-centos-deps:6

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

# prepare 
WORKDIR /opt
RUN git clone https://github.com/mcvine/releaser.git mcvine

# build
WORKDIR /opt/mcvine
RUN PATH=/opt/bin:$PATH BOOSTPYTHON_INCDIR=/opt/include BOOSTPYTHON_LIBDIR=/opt/lib GSL_INCDIR=/usr/include GSL_LIBDIR=/usr/lib64  /opt/bin/python2.7 ./build.py
