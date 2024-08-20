# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
  require   => Package['nginx'],
}

# Ensure Apache is not running (if you want to disable Apache)
service { 'apache2':
  ensure => stopped,
  enable => false,
  require => Package['apache2'],
}

# Basic Nginx configuration (if needed)
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable Nginx site
exec { 'enable_nginx_default_site':
  command => '/usr/sbin/nginx -s reload',
  require => File['/etc/nginx/sites-available/default'],
}
