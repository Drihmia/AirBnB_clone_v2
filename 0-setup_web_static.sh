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

apt-get -y update
apt-get -y install nginx

list_directories=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")

# creating the list of directories
for dir in "${list_directories[@]}";
do
	if [ ! -d "$dir" ]; then
		if mkdir -m 755 "$dir";
		then
			echo "-- done creating $dir"
		fi
	else
		echo "-- $dir does exist"
	fi
done

# creating a fake html file
direct="/data/web_static/releases/test"
if [ -d "$direct/" ];
then
	touch -m 666 "$direct/index.html"
	if echo "Hello from NGINX server" > "$direct/index.html"; then
		echo "-- fake html has been created"
	fi
	chmod 755 "$direct/index.html"

fi

# create a symbolic link if it is not existing, otherwise recreate
distination="/data/web_static/current"
source="/data/web_static/releases/test/"

if [ -L "$distination" ]; then
	echo "-- symbolic link $distination already exist"
	echo "-- remove it"
	if rm "$distination"; then
		echo "-- symbolic has been removed"
	else
		echo "-- failed to remove the symbolic link"
		exit 1
	fi
	echo "-- create it"
	if ln -s "$source"  "$distination"; then
		echo "-- symbolic link has been successfully created"
	else
		echo "-- failed to create the symbolic link"
	fi
else
	echo "-- creating the inexistent link"
	if ln -s "$source"  "$distination"; then
		echo "-- symbolic link has been successfully created"
	else
		echo "-- failed to create the symbolic link1"
	fi
fi

# Give ownership of the /data/ folder to the ubuntu user AND group
echo "-- test chowm"
if chown -R ubuntu:ubuntu "/data/"; then
	echo "-- the change owner has been done successfully"
else
	echo "-- changing owner: something went wrong"
fi

# Update nginx configuration te serve new content under /hbnb_static

new_str="server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"

sed -i 's/server_name _;/'"$new_str"'/' /etc/nginx/sites-available/default

nginx -s reload
