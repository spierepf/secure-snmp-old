FROM ubuntu
ADD . /code
WORKDIR /code

RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" > /etc/apt/sources.list.d/multiverse.list
RUN apt-get update
RUN apt-get install apt-utils -y --no-install-recommends

RUN apt-get install openssh-server snmp snmp-mibs-downloader -y --no-install-recommends
RUN mkdir /var/run/sshd

RUN apt-get install python-minimal python-setuptools python-pip -y --no-install-recommends
RUN pip install flask
RUN pip install redis

CMD ["python", "app.py"]
