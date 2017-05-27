# Changes the amount of open file processess for server
exec { '-n 15 to - Hn':
  path    => ['/usr/bin/','/usr/sbin/','/bin'],
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"- Hn\"/" /etc/default/nginx && service nginx restart',
}