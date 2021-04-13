-- configure the server to response with a new header
file_line { 'Config'
  ensure => 'present'
  path => '/etc/nginx/sites-available/default'
  line => '    add_header X-Server-By $HOSTNAME;'
}
