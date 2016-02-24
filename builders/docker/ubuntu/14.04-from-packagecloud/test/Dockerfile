FROM linjiao/mcvine-ubuntu-install-from-packagecloud:14.04

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to test MCViNE installed from package cloud"

RUN apt-get install -qy build-essential
RUN apt-get install -qy cmake
RUN apt-get install -qy git
RUN apt-get install -qy wget
WORKDIR /opt/danse/share/mcvine/tests
RUN wget -O CMakeLists.txt https://raw.githubusercontent.com/mcvine/mcvine/master/builders/runtests-CMakeLists.txt
RUN mkdir build
WORKDIR /opt/danse/share/mcvine/tests/build
