#!/usr/bin/env bash
set -e

python -m flask --app flaskr run --host=127.0.0.1 --port=8080 --debugger --reload