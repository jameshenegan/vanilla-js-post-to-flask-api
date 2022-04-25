The purpose of this project is set up Nginx on an Ubuntu server.

Ngnix will serve a static web page. The web page will be able to make a POST request to a Flask API.

```
sudo apt update
sudo ufw enable
sudo ufw allow ssh
git clone https://github.com/jameshenegan/vanilla-js-post-to-flask-api.git

sudo apt install nginx
sudo ufw allow 'Nginx HTTP'
vim site-config.nginx

cp site-config.nginx /etc/nginx/sites-available/site-config.nginx
sudo cp site-config.nginx /etc/nginx/sites-available/site-config.nginx
sudo ln -s /etc/nginx/sites-available/site-config.nginx /etc/nginx/sites-enabled/site-config.nginx
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl reload nginx

sudo apt install python3-pip
pip3 install flask
python3 app.py
pip3 install gunicorn
vim app.py
ls
python3 app.py
home/ubuntu/.local/bin/gunicorn -b 0.0.0.0:5000 wsgi:app
```
