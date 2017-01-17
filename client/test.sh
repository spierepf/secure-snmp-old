#!/bin/bash

SERVER=server

#rm -f /tmp/client.json /root/.ssh/id_rsa /root/.ssh/id_rsa.pub

if [ ! -f /root/.ssh/id_rsa ] ; then
    ssh-keygen -N "" -f /root/.ssh/id_rsa
    rm -f /tmp/client.json
fi

if [ ! -f /tmp/client.json ] ; then
    curl -H "Content-Type: application/json" -X POST -d "{\"client_public_key\":\"`cat /root/.ssh/id_rsa.pub`\"}" http://$SERVER:5000/securesnmp/api/v1.0/client > /tmp/client.json
    echo $SERVER `jq -r .client.server_public_key /tmp/client.json` > /root/.ssh/known_hosts
    ssh-keygen -Hf /root/.ssh/known_hosts
    rm -f /root/.ssh/known_hosts.old
fi

ssh -t `jq -r .client.uuid /tmp/client.json`@$SERVER
