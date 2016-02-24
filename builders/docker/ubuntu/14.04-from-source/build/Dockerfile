FROM linjiao/mcvine-ubuntu-deps:14.04

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to build MCViNE"

# prepare 
RUN mkdir -p /src
WORKDIR /src
RUN git clone https://github.com/mcvine/mcvine

# build
# /src/mcvine: source code
# /src/mcvine/build: build dir
# /opt/danse: install prefix
RUN mkdir -p /src/mcvine/build
WORKDIR /src/mcvine/
RUN ./builders/build $PWD $PWD/build /opt/danse /opt/danse/share/mcvine/resources
