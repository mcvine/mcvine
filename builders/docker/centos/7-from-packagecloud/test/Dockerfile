FROM linjiao/mcvine-centos-install-from-packagecloud:7

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to test MCViNE installed from package cloud"

RUN yum -y groupinstall "Development tools"
RUN yum -y install which
RUN yum -y install cmake git wget
WORKDIR /opt/danse/share/mcvine/tests
RUN wget -O CMakeLists.txt https://raw.githubusercontent.com/mcvine/mcvine/master/builders/runtests-CMakeLists.txt
RUN mkdir build
WORKDIR /opt/danse/share/mcvine/tests/build
