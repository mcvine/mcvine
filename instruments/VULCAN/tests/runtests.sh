#!/usr/bin/env bash

# Add directory to PYTHONPATH first
export PWD=`pwd`
export PYTHONPATH="${PWD}/../applications"

python mcstas_converter_TestCase.py
