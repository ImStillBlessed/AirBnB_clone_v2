#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html > dev/null

# create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership for the folder to the server user
sudo chowm -R ubuntu:ubuntu /data/

sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
