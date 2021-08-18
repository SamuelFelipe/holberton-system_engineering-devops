# install and configure nginx

$cmd = @("Command"/L)
  new_string="\n\n\tlocation \/redirect_me {\n\t\treturn 301 Holberton School;\n\t}\n"
  ALREADY_IN=$( grep "redirect_me" /etc/nginx/sites-available/default)

  if [[ -z $ALREADY_IN ]]; then
    sudo sed -i "s/root \/var\/www\/html;/root \/var\/www\/html;$new_string/" /etc/nginx/sites-available/default
    sudo service nginx restart
  fi
 | - Command

exec {
  command => 'sudo apt-get update; sudo apt-get install nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec {
  command =>   
  path    => '/usr/local/bin/:/bin/'
}
