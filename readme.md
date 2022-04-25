The purpose of this project is to set up Nginx on an Ubuntu server. Ngnix will serve a static web page. The web page will be able to make a POST request to a Flask API.

# Setup

Setup the Ubuntu server.

```
sudo apt update
sudo ufw enable
sudo ufw allow ssh

```

Copy this project over to the Ubuntu server.

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
