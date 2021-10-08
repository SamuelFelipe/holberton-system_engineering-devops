# solve a problem
exec {
  path    =>    '/usr/bin:/bin',
  command =>    'sed -i "s/5/50000/" /etc/security/limits.conf; sed -i "s/4/40000/" /etc/security/limits.conf',
}
