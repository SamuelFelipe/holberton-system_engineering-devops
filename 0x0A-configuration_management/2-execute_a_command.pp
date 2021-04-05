# kill a program
exec {
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
