#!/bin/bash

CURRENT_DIR=$(pwd)
docker run -v "$CURRENT_DIR":/work --rm juplab:310 python3 scripts/quote.py >> logs/test_quote.log
