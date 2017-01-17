FROM ubuntu
ADD . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install apt-utils -y --no-install-recommends

RUN apt-get install openssh-server ppp -y --no-install-recommends
RUN mkdir /var/run/sshd

RUN apt-get install python-minimal python-setuptools python-pip -y --no-install-recommends
RUN pip install flask

CMD ["python", "app.py"]
