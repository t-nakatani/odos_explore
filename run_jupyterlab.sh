#!/bin/bash

CURRENT_DIR=$(pwd)
docker run -d -v "$CURRENT_DIR":/work --rm -p 8088:8088 juplab:310 jupyter-lab --port=8088 --ip=0.0.0.0 --allow-root --no-browser
