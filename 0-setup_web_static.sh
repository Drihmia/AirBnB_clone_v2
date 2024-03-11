#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static.
# It must:
# 1. Install Nginx if it's not already installed
# 2. Create necessary directories if they don't exist
# 3. Create a fake HTML file for testing
# 4. Create symbolic link and ensure it's always up to date
# 5. Set ownership of /data/ to ubuntu user and group
# 6. Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
#    Don't forget to restart Nginx after updating the configuration


# check if nginx is install otherwise install it
if ! command -v nginx >/dev/null 2>&1; then
	apt-get -y install nginx
fi

list_directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

# creating the list of directories
for dir in "${list_directories[@]}";
do
	if [ ! -d "$dir" ]; then
		mkdir -m 755 "$dir"
	fi
done

# creating a fake html file
direct="/data/web_static/releases/test"
if [ -d "$direct/" ];
then
	touch -m 755 "$direct/index.html"
	echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "$direct/index.html"
	# chmod 755 "$direct/index.html"

fi

# create a symbolic link if it is not existing, otherwise recreate
distination="/data/web_static/current"
source="/data/web_static/releases/test/"

if [ -L "$distination" ]; then
	rm "$distination"
	ln -s "$source"  "$distination"
else
	ln -s "$source"  "$distination"
fi

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu "/data/"

# Update nginx configuration te serve new content under /hbnb_static/

hbnb_static_f_str="server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
nginx_config="/etc/nginx/sites-available/default"

if ! grep -q "location /hbnb_static/ " "$nginx_config"; then
	sed -i 's/server_name _;/'"$hbnb_static_f_str"'/'  "$nginx_config"
fi
# Update nginx configuration te serve new content under /hbnb_static

hbnb_static_str="server_name _;\n\tlocation \/hbnb_static {\n\t\treturn 301 \/hbnb_static\/;\n\t}"
nginx_config="/etc/nginx/sites-available/default"

if ! grep -q "location /hbnb_static " "$nginx_config"; then
	sed -i 's/server_name _;/'"$hbnb_static_str"'/'  "$nginx_config"
fi


nginx -s reload

exit 0
