# This kills a process named killmenow
#Author: Oumayma Mazoz

exec { 'process kill killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}
