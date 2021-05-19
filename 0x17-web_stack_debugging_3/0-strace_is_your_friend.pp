exec { 'change':
  path    => '/usr/local/bin'
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
