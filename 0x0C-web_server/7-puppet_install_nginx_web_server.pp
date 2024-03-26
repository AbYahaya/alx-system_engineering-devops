# Define package resources to install nginx
package { 'nginx':
  ensure => installed,
}

# Define service resources to manage nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define file resource for the nginx default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define template for the nginx default site configuration
# This template includes both the "Hello World!" page and the redirection configuration
# You can place this template file in the same directory as your manifest file
# Let's name it default.erb

# Contents of default.erb:

# server {
#     listen 80 default_server;
#     listen [::]:80 default_server;
#     root /var/www/html;
#     index index.html index.htm;
#     server_name _;
# 
#     location / {
#         try_files $uri $uri/ =404;
#         # Return "Hello World!" page
#         add_header Content-Type text/html;
#         return 200 "<!DOCTYPE html><html><head><title>Hello World!</title></head><body><h1>Hello World!</h1></body></html>";
#     }
# 
#     location /redirect_me {
#         # Perform a 301 redirect to the specified URL
#         return 301 https://www.example.com/new_page;
#     }
# }
