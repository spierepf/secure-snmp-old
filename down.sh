#!/bin/bash

docker-compose down
docker rm securesnmp_cloud_1
docker rm securesnmp_transmitter_1
docker rm securesnmp_redis_1
docker rmi securesnmp_cloud
docker rmi securesnmp_transmitter
