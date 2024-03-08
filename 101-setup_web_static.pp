# puppet manifest to set up web servers for the deployment of web_static

# ensure nginx package is installed
package { 'nginx':
  ensure => installed,
}

# define necessary directories
$directories = [
  '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]

# create necessary directories
$directories.each |$dir| {
  file { $dir:
    ensure => directory,
    mode   => '0755',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }
}

# create a fake html file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    holberton school
  </body>
</html>',
  mode    => '0755',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# create or update symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/'],
}

# update nginx configuration
$file_contents = file('/etc/nginx/sites-available/default').content
if !($file_contents =~ /location \/hbnb_static\//) {
  file_line { 'nginx_hbnb_static_location':
    path  => '/etc/nginx/sites-available/default',
    line  => '  location /hbnb_static/ {',
    match => '^server_name _;$',
  }

  file_line { 'nginx_hbnb_static_alias':
    path  => '/etc/nginx/sites-available/default',
    line  => '    alias /data/web_static/current/;',
    after => '  location /hbnb_static/ {',
  }
}

# reload nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File_line['nginx_hbnb_static_location', 'nginx_hbnb_static_alias'],
  notify  => Exec['nginx_reload'],
}

exec { 'nginx_reload':
  command     => 'nginx -s reload',
  refreshonly => true,
}

