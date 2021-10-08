# solve a problem
exec {
  path    =>    '/usr/bin:/bin',
  command =>    'sed -i "s/holberton/foo/" /etc/security/limits.conf',
}
