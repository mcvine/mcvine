FROM centos:6

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image prepared for buildindg MCViNE"

# installation of basic software and dependencies
RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y groupinstall "Development tools"

# deps for python
RUN yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
# install python
RUN yum install -y wget tar
RUN mkdir -p /opt/src
WORKDIR /opt/src
RUN wget http://python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
RUN tar xf Python-2.7.9.tar.xz
WORKDIR /opt/src/Python-2.7.9
RUN mkdir -p /opt/lib /opt/bin
RUN ./configure --prefix=/opt --enable-shared LDFLAGS="-Wl,-rpath /opt/lib"
# RUN ./configure --prefix=/opt --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /opt/lib"
RUN make && make altinstall
# add python
RUN ln /opt/bin/python2.7 /opt/bin/python

# pip
WORKDIR /opt/src
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN /opt/bin/python2.7 get-pip.py

# python packages
RUN /opt/bin/pip install -U numpy psutil 

# h5py
RUN yum -y install hdf5-devel
RUN /opt/bin/pip install -U h5py 

# boost python
RUN wget http://downloads.sourceforge.net/project/boost/boost/1.58.0/boost_1_58_0.tar.gz
RUN tar xfz boost_1_58_0.tar.gz
WORKDIR boost_1_58_0
RUN ./bootstrap.sh --with-libraries=python --with-python=/opt/bin/python2.7 --prefix=/opt
RUN ./b2
RUN ./b2 install

# gsl
RUN yum install -y install gsl gsl-devel

# srcctrl
RUN yum install -y git

