#!/bin/bash

# Simple docker script for editing the slides

# It spins up an Apache httpd, serves the slides and cleans
# up the container once you Ctrl-C it. Run it, and view slides 
# on http://localhost:8000/

# Tell SELinux it's okay for the container to access these files..
chcon -Rt svirt_sandbox_file_t .

# build and run the container, so simple there's no Dockerfile
docker run --rm -it --name my-apache-app \
  -v "$PWD":/usr/local/apache2/htdocs/ -p 8000:80 httpd:2.4

