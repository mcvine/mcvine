FROM linjiao/mcvine-ubuntu-install-from-packagecloud:14.04

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to test MCViNE installed from package cloud"

RUN apt-get install -qy build-essential
RUN apt-get install -qy cmake
RUN apt-get install -qy git
WORKDIR /opt/danse/share/mcvine/resources/tests
RUN mkdir build
WORKDIR /opt/danse/share/mcvine/resources/tests/build
RUN cmake ..
RUN make test ARGS="-j `grep -c ^processor /proc/cpuinfo`"
