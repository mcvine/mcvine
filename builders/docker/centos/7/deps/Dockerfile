##### THIS IS NOT WORKING YET #####

FROM centos:7

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image prepared for buildindg MCViNE"

# installation of basic software and dependencies
# 
# dev
RUN yum install -y git gcc-c++ make
# dependencies: packages
RUN yum install -y python python-devel numpy 
RUN easy_install psutil
# hdf5 need additional stuff
RUN rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt
RUN yum install http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
RUN easy_install h5py
# dependencies: c libs
RUN yum install -y install gsl gsl-devel
# dependencies: boost python
RUN yum install -y boost-devel boost-python


# prepare 
RUN mkdir -p /opt
WORKDIR /opt
RUN git clone https://github.com/mcvine/releaser.git mcvine
# WORKDIR /opt/mcvine
# RUN BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib64 ./build.py
