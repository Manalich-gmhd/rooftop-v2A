#!/bin/bash

#sudo apt update && sudo apt dist-upgrade
/usr/bin/python3 -m pip install --upgrade pip
pip3 install flask
export PATH="/home/CCSI/.local/bin:$PATH"
pip3 install flask-cors
pip3 install gevent
