FROM ubuntu
ADD . /code
WORKDIR /code

RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" > /etc/apt/sources.list.d/multiverse.list
RUN apt-get update
RUN apt-get install apt-utils -y --no-install-recommends

RUN apt-get install vim openssh-client curl jq snmpd snmp-mibs-downloader -y --no-install-recommends
RUN echo "agentAddress  tcp:127.0.0.1:161" >> /etc/snmp/snmpd.conf

#CMD ["tail", "-f", "/dev/null"]
CMD ["/usr/sbin/snmpd", "-L", "-f", "-u", "snmp", "-g", "snmp", "-I", "-smux,mteTrigger,mteTriggerConf", "-p", "/run/snmpd.pid"]