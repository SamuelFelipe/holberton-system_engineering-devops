exec { 'change':
  path    =>   '/usr/bin/env:/bin/',
  command =>   'sed -i s/15/1000/ /etc/default/nginx',
}
