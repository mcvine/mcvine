FROM linjiao/mcvine-fedora-install-from-packagecloud:21

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to install MCViNE"

# build essential
RUN yum install -y make automake gcc gcc-c++ kernel-devel

RUN yum install -y cmake
RUN yum install -y git
RUN yum install -y wget
WORKDIR /opt/danse/share/mcvine/tests
RUN wget -O CMakeLists.txt https://raw.githubusercontent.com/mcvine/mcvine/master/builders/runtests/CMakeLists.txt
RUN mkdir build
WORKDIR /opt/danse/share/mcvine/tests/build
