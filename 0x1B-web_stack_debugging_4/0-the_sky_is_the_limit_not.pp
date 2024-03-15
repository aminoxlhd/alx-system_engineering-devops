# fix our stack so that we get to 0

file { '/etc/default/nginx':
  ensure  => present,
  content => template('module_name/nginx_config.erb'),
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  refreshonly => true,
}
