#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py --force-reinstall

brew install portaudio

pip install sentencepiece

pip install -r source/requirements.txt

python3 source/main.py
