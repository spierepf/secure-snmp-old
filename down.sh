#!/bin/bash

docker-compose down
docker rm securesnmp_server_1
docker rm securesnmp_transmitter_1
docker rmi securesnmp_server
docker rmi securesnmp_transmitter
