exec { 'kill':
  command  => 'pkill -f test',
  provider => 'shell'
}