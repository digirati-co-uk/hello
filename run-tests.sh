#!/bin/sh

set -e

python -m pytest
python -m pylint app tests
python -m flake8 app tests