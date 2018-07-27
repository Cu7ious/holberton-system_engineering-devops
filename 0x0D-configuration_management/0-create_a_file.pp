# create a file in /tmp.
  # path is /tmp/holberton
  # permission is 0744
  # owner is www-data
  # group is www-data
  # contains I love Puppet

file { '/tmp/holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
