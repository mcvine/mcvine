FROM linjiao/mcvine-ubuntu-deps:14.04

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

# prepare 
RUN mkdir -p /src
WORKDIR /src
RUN git clone https://github.com/mcvine/mcvine

# build
RUN mkdir -p /src/mcvine/build
WORKDIR /src/mcvine/
RUN ./builders/build $PWD $PWD/build /opt/mcvine 
