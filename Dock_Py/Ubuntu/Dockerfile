FROM ubuntu:20.04
RUN apt-get update 
RUN apt-get install python3 -y
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements-pip.txt /root/requirements-pip 
COPY requirements-apt.txt /root/requirements-apt
COPY read.py /root/read.py
COPY Dock_Files/* /root/Dock_Files 

RUN pip3 install -r /root/requirements-pip
RUN python /root/read.py
