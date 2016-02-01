FROM ubuntu:14.04

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image prepared for buildindg MCViNE"

# installation of basic software and dependencies
RUN apt-get update
# 
# dependencies: packages
RUN apt-get -qy install python python-numpy python-psutil python-h5py python-mpi4py
# dependencies: c libs
RUN apt-get -qy install libgsl0-dev 
# dependencies: boost python
RUN apt-get -qy install libboost-python-dev libboost-python1.55.0
# dev
RUN apt-get -qy install git g++ make

# cmake
RUN apt-get -qy install cmake

# danse ins pkgs
RUN apt-get -qy install curl
RUN curl -s https://packagecloud.io/install/repositories/danse/ins/script.deb.sh |  bash
RUN apt-get -qy install pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops
