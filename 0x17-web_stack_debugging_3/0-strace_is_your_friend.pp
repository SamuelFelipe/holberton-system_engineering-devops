# change wrong path at wp-settings.php
exec { 'change':
  path    => '/usr/bin/:/bin/',
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
