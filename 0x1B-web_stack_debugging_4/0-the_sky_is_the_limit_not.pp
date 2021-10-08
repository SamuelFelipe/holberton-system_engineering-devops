# solve a problem
exec { 'change':
  path    =>   '/usr/bin:/bin',
  command =>   'sed -i s/15/10000/ /etc/default/nginx; service nginx restart',
}
