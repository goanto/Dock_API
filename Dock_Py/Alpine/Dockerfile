FROM python:3.9.0-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements-pip.txt /root/requirements-pip 
COPY requirements-apk.txt /root/requirements-apk
COPY read.py /root/read.py
COPY Dock_Files/* /root/Dock_Files 

RUN pip3 install -r /root/requirements-pip
RUN python /root/read.py
