#!/usr/bin/env bash
"""This is the script for AirBnB"""

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo "<h1>Holberton School</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "41i " /etc/nginx/sites-available/default 
sudo service nginx restart