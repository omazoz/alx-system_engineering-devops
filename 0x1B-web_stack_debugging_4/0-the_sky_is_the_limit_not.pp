#we got this file
exec {'sets file limite for nginx':
  command => 'sed -i "s/15/4096/g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/default/nginx'
}
