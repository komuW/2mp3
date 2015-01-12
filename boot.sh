#!/usr/bin/env bash
#
# Set up/ Provision a Vagrant Ubuntu Precise box

echo "setup...."

sudo apt-get update && \
sudo apt-get -y install python-software-properties \
software-properties-common \
git \
gcc \
lynx-cur \
build-essential \
python-dev \
python-setuptools \
python-pip \
curl && \
sudo pip install --upgrade pip 
sudo pip install virtualenv virtualenvwrapper
virtualenv /vagrant/venv
