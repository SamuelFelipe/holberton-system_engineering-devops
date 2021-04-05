# create a file
file {'/etc/holberton':
  ensure  => 'directory',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
