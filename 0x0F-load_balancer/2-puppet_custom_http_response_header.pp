#!/usr/bin/env bash
# configure the server to response with a new header
exec {
  command => 'sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install nginx'
  provider => shell
}

file_line { 'Config'
  ensure => 'present'
  path => '/etc/nginx/sites-available/default'
  line => '    add_header X-Server-By $HOSTNAME;'
}
