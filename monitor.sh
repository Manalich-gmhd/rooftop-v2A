#!/bin/bash
sudo apt install supervisor
sudo cp gmhd.conf /etc/supervisor/conf.d
sudo supervisorctl reload