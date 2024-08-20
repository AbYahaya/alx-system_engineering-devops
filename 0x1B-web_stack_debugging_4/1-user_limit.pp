# Puppet manifest to increase open file limits for the holberton user

file_line { 'holberton nofile soft':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 65535',
  match => '^holberton soft nofile',
}

file_line { 'holberton nofile hard':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 65535',
  match => '^holberton hard nofile',
}
