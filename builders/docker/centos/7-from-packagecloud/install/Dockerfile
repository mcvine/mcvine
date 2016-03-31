FROM centos:7

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to install MCViNE"

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all

RUN yum -y install deltarpm

RUN curl -s https://packagecloud.io/install/repositories/danse/ins/script.rpm.sh | bash
RUN yum install -qy mcvine
