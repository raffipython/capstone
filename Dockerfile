FROM debian:buster

RUN apt update && apt install python3.8 -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 user 

RUN echo 'user:password' | chpasswd

# Add installing extra packages here to build the capstone template
# Example:
#RUN apt install -y <PACKAGE_NAME>
