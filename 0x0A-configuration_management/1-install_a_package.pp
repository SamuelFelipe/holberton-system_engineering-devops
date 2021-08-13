# Install puppet
exec {
  command => 'gem install puppet-lint -v 2.1.1',
  path    => '/usr/local/bin/:/bin/'
}
