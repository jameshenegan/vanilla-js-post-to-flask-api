# Introduction

The purpose of this project is to set up Nginx on an Ubuntu server. Ngnix will serve a static web page. The web page will use vanilla JavaScript to make a POST request to a Flask API.

# Project Organization

- The `api` directory has the code for the Flask API.
- The `frontend` directory has the static web page.
- The `site-config.nginx` file has the Nginx congifuration.

The rest of this `readme.md` file explains how to set up the project.

# Setup

Begin by connecting to a "fresh" Ubuntu server.

- I am using AWS to create an EC2 instance.
  - Ubuntu 20.04 image
  - Newtork settings: allow SSH, HTTPS, and HTTP traffic

Once you have connected, update packages and setup the firewall.

```
sudo apt update
sudo ufw enable
sudo ufw allow ssh
```

Now copy this project from github over to the Ubuntu server.

```
git clone https://github.com/jameshenegan/vanilla-js-post-to-flask-api.git
```

Set up Nginx

```
sudo apt install nginx
sudo ufw allow 'Nginx HTTP'
cd vanilla-js-post-to-flask-api
sudo cp site-config.nginx /etc/nginx/sites-available/site-config.nginx
sudo ln -s /etc/nginx/sites-available/site-config.nginx /etc/nginx/sites-enabled/site-config.nginx
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl reload nginx
```

Set up Python

```
sudo apt install python3-pip
sudo apt install python3.8-venv
cd api
python3 -m venv venv
source venv/bin/activate
pip3 install flask
pip3 install gunicorn
gunicorn -b 0.0.0.0:5000 wsgi:app
```
