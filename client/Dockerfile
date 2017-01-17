FROM ubuntu
ADD . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install apt-utils -y --no-install-recommends

RUN apt-get install vim openssh-client curl jq ppp -y --no-install-recommends

CMD ["tail", "-f", "/dev/null"]
