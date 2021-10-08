# solve a problem
exec { 'change':
  path    =>   '/usr/bin/env:/bin/',
  command =>   'sed -i s/15/10000/ /etc/default/nginx',
}
