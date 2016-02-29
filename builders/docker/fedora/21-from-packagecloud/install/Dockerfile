FROM fedora:21

MAINTAINER "Jiao Lin <jiao.lin@gmail.com>"

LABEL Description="image to install MCViNE"

RUN yum install -y deltarpm

RUN yum install -y curl
RUN curl -s https://packagecloud.io/install/repositories/danse/ins/script.rpm.sh | bash
RUN yum install -y mcvine
