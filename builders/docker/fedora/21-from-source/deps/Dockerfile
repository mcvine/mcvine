FROM fedora:21

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image prepared for buildindg MCViNE"

# installation of basic software and dependencies
# 
# dependencies: packages
RUN yum install -y python python-devel numpy python-psutil h5py
RUN yum install -y mpi4py-mpich
# mpi4py is not in path by default in fedora
WORKDIR /usr/lib64/python2.7/site-packages/
RUN ln -s mpich/mpi4py mpi4py
# dependencies: c libs
RUN yum install -y install gsl gsl-devel
# dependencies: boost python
RUN yum install -y boost-devel boost-python
# dev
RUN yum install -y git gcc-c++ make

