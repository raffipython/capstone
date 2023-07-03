#!/bin/bash

# Using a Debian Linux host
sudo apt-get -y install terminator docker docker-compose
sudo docker pull debian:buster
sudo docker build -t capstone .

pip install -U cmd2

