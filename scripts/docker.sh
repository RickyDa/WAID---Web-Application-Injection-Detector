#!/bin/bash

cd ~/WAID---Web-Application-Injection-Detector

docker-compose down

git pull

./scripts/remove_pull_up.sh

docker-compose up --build
