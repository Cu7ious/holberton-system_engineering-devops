# A manifest that kills a process named killmenow using puppet
  # Must use the exec Puppet resource
  # Must use pkill

exec {'killmenow':
  command => pkill -f killmenow
}
