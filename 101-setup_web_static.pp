# File: 101-setup_web_static.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define directories to be created
$directories = [
  '/data',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/shared',
  '/data/web_static/releases/test',
]

# Create necessary directories
file { $directories:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<html><head><title>Test Page</title></head><body><h1>This is a test page.</h1></body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}


# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @(EOF),
    # Nginx configuration
    
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        root /var/www/html;

        location /hbnb_static/ {
            alias /data/web_static/current/;
        }
    }
  EOF

  require => Package['nginx'],
  notify  => Service['nginx'],
}


# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

