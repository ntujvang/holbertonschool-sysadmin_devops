# This puppet manifest creates a file inside /tmp with I love Puppet
file {'/tmp/holberton':,
  ensure  => file,
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}