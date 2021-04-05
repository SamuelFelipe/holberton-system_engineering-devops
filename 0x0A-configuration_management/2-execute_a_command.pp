# kill a program
exec {
  command => 'pkill -x killmenow',
  path    => '/usr/bin'
}
