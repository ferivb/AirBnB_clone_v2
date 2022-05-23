#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
# Adds a custom 301 redireection page and custom 404 message
# Adds header = to X-Served-By $HOSTNAME
# shellcheck disable=SC2154

#updates apt repo
sudo apt-get update -y

# Installs nginx
sudo apt-get install nginx -y

# Creates the data directory and its children
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Symlink for the test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#unlinks the default file
unlink /etc/nginx/sites-enabled/default

#creates the config file
echo "server {
	listen 80 default_server;
	index index.html;
	server_name ferivb.tech;
	root /var/www/ferivb.tech/html;
        add_header X-Served-By $HOSTNAME;
	location /redirect_me {
                return 301 https://www.youtube.com/watch?v=LFfVDyW6ddg\$request_uri;
        }
	error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/ferivb.tech/html;
                internal;
        }
        location /hbnb_static/ {
                alias /data/web_static/current/;
        }
	}
" > /etc/nginx/conf.d/ferivb.tech.conf

#creates the index file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html;

#creates the index file
echo "Ceci n'est pas une page" > /var/www/ferivb.tech/html/custom_404.html;

# Give ownership to ubuntu user/group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

#restarts the server
sudo service nginx restart