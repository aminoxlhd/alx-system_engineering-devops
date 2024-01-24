# Install Nginx web server

class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 http://new-redirect-url;
    }
}
",
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => '<html><body><h1>Hello World!</h1></body></html>',
  }
}

include nginx_server
