# Introduction

The purpose of this project is to set up Nginx on an Ubuntu server. Ngnix will serve a static web page. The web page will use vanilla JavaScript to make a POST request to a Flask API.

# Project Organization

- The `api` directory has the code for the Flask API.
- The `frontend` directory has the static web page.
- The `site-config.nginx` file has the Nginx congifuration.

The rest of this `readme.md` file explains how to set up the project.

# Setup

## Setting up a Server

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

## Copying over the Project

Now copy this project from github over to the Ubuntu server.

```
git clone https://github.com/jameshenegan/vanilla-js-post-to-flask-api.git
```

# Nginx

## Installation

```
sudo apt install nginx
```

## Setup

```
sudo ufw allow 'Nginx HTTP'
```

You can try to access the server from your web browser. You should see the default Nginx page.

## Configuration

We will copy our configuration over to the place where it's supposed to go

```
cd vanilla-js-post-to-flask-api
sudo cp site-config.nginx /etc/nginx/sites-available/site-config.nginx
```

Now we make a symbolic link from our configuration in the `sites-available` directory over to the `sites-enabled` directory

```
sudo ln -s /etc/nginx/sites-available/site-config.nginx /etc/nginx/sites-enabled/site-config.nginx
```

We can get rid of the default site.

```
sudo rm /etc/nginx/sites-enabled/default
```

## Reload

Now we tell our server to reload Nginx.

```
sudo systemctl reload nginx
```

# Set up Python

We need to install the python package manager.

```
sudo apt install python3-pip
```

We will use virtual environments, since they seem to help out with `gunicorn`. First we install the `venv` module.

```
sudo apt install python3.8-venv
```

Now we create a virtual environment.

```
cd api
python3 -m venv venv
```

Then we activate the virtual environment.

```
source venv/bin/activate
```

Now that the environment is activated, we can install our packages.

```
pip3 install flask
pip3 install gunicorn
```

Finally, we can run `gunicorn`.

```
gunicorn -b 0.0.0.0:5000 wsgi:app
```

Everything should work now.
