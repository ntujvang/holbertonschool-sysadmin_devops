#Puppet manifest that solves an issue using "strace"
exec { 'php_file':
  command => 'sed -ie 's@locale.phpp@locale.php@' /var/www/html/wp-settings.php'
}